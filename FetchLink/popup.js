document.addEventListener('DOMContentLoaded', function () {
    var button = document.getElementById('myButton');

    button.addEventListener('click', function () {
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            var currentUrl = tabs[0].url;

            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'http://localhost:5000/scrape');
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            xhr.onreadystatechange = function () {
                if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                    var scrapedData = JSON.parse(xhr.responseText);

                    // Additional: Send scrapedData to the machine learning model
                    sendToMLModel(scrapedData);
                }
            };
            xhr.send('currentUrl=' + currentUrl);
        });
    });

    // Additional function to send data to the machine learning model
    function sendToMLModel(scrapedData) {
        // Assume mlModelEndpoint is the endpoint for your machine learning model
        var mlModelEndpoint = 'http://127.0.0.1:5002';

        var xhrML = new XMLHttpRequest();
        xhrML.open('POST', mlModelEndpoint);
        xhrML.setRequestHeader('Content-Type', 'application/json');
        xhrML.onreadystatechange = function () {
            if (xhrML.readyState === XMLHttpRequest.DONE && xhrML.status === 200) {
                var mlResult = JSON.parse(xhrML.responseText);
                updateNewDocWithMLResult(scrapedData, mlResult);
            }
        };
        xhrML.send(JSON.stringify(scrapedData));
    }

    // Additional function to update newDoc with machine learning result
    function updateNewDocWithMLResult(scrapedData, mlResult) {
        var newDoc = document.implementation.createHTMLDocument('Scraped Links');

        var header = newDoc.createElement('h1');
        header.textContent = 'Scraped Links:';
        newDoc.body.appendChild(header);

        scrapedData.forEach(function (data, index) {
            var linkElement = newDoc.createElement('p');
            linkElement.textContent = data.url + ': ' + data.status + ' | Phishing Score: ' + mlResult[index].phishing_score.toFixed(2) + '%';
            newDoc.body.appendChild(linkElement);
        });

        var htmlString = new XMLSerializer().serializeToString(newDoc);

        var newTab = window.open();
        newTab.document.write(htmlString);
    }
});

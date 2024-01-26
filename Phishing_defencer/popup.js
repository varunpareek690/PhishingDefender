document.addEventListener('DOMContentLoaded', function () {
    // Get the button element
    var button = document.getElementById('myButton');

    // Add a click event listener to the button
    button.addEventListener('click', function () {
        // Get the current tab
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            // Get the URL of the current tab
            var currentUrl = tabs[0].url;

            // Make an AJAX request to your Python Flask server
            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'http://localhost:5000/scrape');
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            xhr.onreadystatechange = function () {
                if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                    // Parse the JSON response
                    var scrapedData = JSON.parse(xhr.responseText);



                    
                    
                    var linksString = 'Scraped Links:\n\n';
                    
                    scrapedData.forEach(function (data) {
                        linksString += data.url + ': ' + data.status + '\n';
                    });
                    
                    // Show an alert with the links
                    alert(linksString);
                }
            };
            xhr.send('currentUrl=' + currentUrl);
        });
    });
    // #### open a new window in full web page
    // // Create a new HTML document
    // var newDoc = document.implementation.createHTMLDocument('Scraped Links');

    // // Add a header to the new document
    // var header = newDoc.createElement('h1');
    // header.textContent = 'Scraped Links:';
    // newDoc.body.appendChild(header);

    // // Add each scraped link to the new document
    // scrapedData.forEach(function (data) {
    //     var linkElement = newDoc.createElement('p');    
    //     linkElement.textContent = data.url + ': ' + data.status;
    //     newDoc.body.appendChild(linkElement);
    // });

    // // Convert the new document to HTML string
    // var htmlString = new XMLSerializer().serializeToString(newDoc);

    // // Open a new tab with the HTML content
    // var newTab = window.open();
    // newTab.document.write(htmlString);









    // ####  Opens a new tab in window
    // var htmlString = '<h1>Scraped Links:</h1>';

    // scrapedData.forEach(function (data) {
    //     htmlString += '<p>' + data.url + ': ' + data.status + '</p>';
    // });

    // // Open a new popup window with the HTML content
    // var popup = window.open('', '_blank', 'width=600,height=400');
    // popup.document.write(htmlString);
});
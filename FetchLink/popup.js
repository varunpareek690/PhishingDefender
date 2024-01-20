// popup.js
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

                  // Create a new HTML element to display the scraped data
                  var resultWindow = document.createElement('div');

                  // Append each scraped link to the result window
                  scrapedData.forEach(function (data) {
                      var linkElement = document.createElement('p');
                      linkElement.textContent = data.url + ': ' + data.status;
                      resultWindow.appendChild(linkElement);
                  });

                  // Append the result window to the popup
                  document.body.appendChild(resultWindow);
              }
          };
          xhr.send('currentUrl=' + currentUrl);
      });
  });
});

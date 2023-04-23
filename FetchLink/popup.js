document.addEventListener('DOMContentLoaded', function() {
  // Get the button element
  var button = document.getElementById('myButton');

  // Add a click event listener to the button
  button.addEventListener('click', function() {
    // Get the current tab
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      // Get the URL of the current tab
      var currentUrl = tabs[0].url;
      // Display the URL in a popup alert box
      alert("Current URL: " + currentUrl);

      // Make an AJAX request to your Python Flask server
      var xhr = new XMLHttpRequest();
      xhr.open('POST', 'http://localhost:5000/scrape');
      xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
      xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
          var scrapedData = xhr.responseText;
          alert(scrapedData);
        }
      };
      xhr.send('currentUrl=' + currentUrl);
    });
  });
});

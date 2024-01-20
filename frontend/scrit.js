// JavaScript function to scrape links and open a new window
function scrapeAndOpenNewWindow() {
  // Call the Python server to perform scraping
  fetch('/scrape', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({ currentUrl: window.location.href }),
  })
  .then(response => response.json())
  .then(data => {
      // Open a new window
      let newWindow = window.open('', '_blank');

      // Modify the content of the new window
      newWindow.document.write(`
          <!DOCTYPE html>
          <html lang="en">

          <head>
              <title>Systumm Projects</title>
              <link rel="stylesheet" href="style.css">
          </head>

          <body>
              <div class="container">
                  <div class="tab-bar">
                      <div class="tab-title">Systumm Projects</div>
                  </div>
                  <div class="main-body">
                      <div class="logo">
                          <img src="pic/logo.jpg" alt="Logo">
                      </div>
                      <!-- Display the scraped data in the new window -->
                      <div class="scraped-data">${JSON.stringify(data)}</div>
                  </div>

                  <footer>
                      <div class="logo-container">
                          <div class="contact">
                              <!-- Your social media links -->
                          </div>
                      </div>
                  </footer>
              </div>
          </body>

          </html>
      `);
  })
  .catch(error => console.error('Error:', error));
}

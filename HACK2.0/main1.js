function checkPhishing() {
    const urlInput = document.getElementById("url").value;
    const urlArray = urlInput.split("/");
    const domain = urlArray[2];
  
    fetch("phishing_dataset.csv")
      .then((response) => response.text())
      .then((data) => {
        const rows = data.split("\n");
        for (let i = 1; i < rows.length; i++) {
          const cols = rows[i].split(",");
          if (cols[0].includes(domain)) {
            document.getElementById("status").textContent = cols[88];
            return;
          }
        }
        document.getElementById("status").textContent =
          "The site is not yet scanned.";
      });
  }
  
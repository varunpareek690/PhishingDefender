// This file is optional if you don't need any JavaScript functionality for now.
// You can add any necessary JavaScript code here for extension-specific behaviors.

// Function to open the second window
function openSecondWindow() {
    // Create a new window object
    const secondWindow = window.open("second-window.html", "Second Window", "width=500,height=400");
  
    // Add an event listener to the window's close event
    secondWindow.addEventListener("close", () => {
      // Close the first window
      window.close();
    });
  }
  
  // Function to handle the click event on the "Click Me" button
  function handleClickMeButtonClick() {
    // Open the second window
    openSecondWindow();
  }
  
  // Add event listeners to the buttons
  document.querySelector(".click-me").addEventListener("click", handleClickMeButtonClick);
  
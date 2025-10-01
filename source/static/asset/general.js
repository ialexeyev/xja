/* SKILL UP application general scripts */

/* Displaying user image */ 
function displayUserImg(img) {
    if (img.style.scale == "5") {
      img.style.translate = "0 0";
      img.style.scale = "1";
    }
    else {
      // for all screen sizes
      if (window.innerWidth >= 1824) {
        img.style.translate = "-2.8vw 2.8vw"; // Large Screens
      }
      if ((window.innerWidth < 1824) && (window.innerWidth >= 1224)) {
        img.style.translate = "-3vw 3vw"; // Desktop PC
      }
      if((window.innerWidth < 1224) && (window.innerWidth >= 1024)) {
        img.style.translate = "-4vw 4vw"; // Laptop
      }
      if((window.innerWidth < 1024) && (window.innerWidth >= 768)) {
        img.style.translate = "-4.5vw 4.5vw"; // Net Laptop
      }
      if((window.innerWidth < 1024) && (window.innerWidth >= 768) && (window.innerHeight >= 900)) {
        img.style.translate = "-6.3vw 5.9vw"; // Big Pad
      }
      if((window.innerWidth < 768) && (window.innerWidth >= 480)) {
        img.style.translate = "-6.9vw 6.9vw"; // Pad
      }
      if((window.innerWidth < 480) && (window.innerWidth >= 360)) {
        img.style.translate = "-9vw 9vw"; // Smartphone
      }
      if(window.innerWidth < 360) {
        img.style.translate = "-9.2vw 9.2vw"; // Mobile
      }
      img.style.scale = "5";
    }
}

/* Return to home page */
function goHome() {
  window.location.href = "/";
}

/* Return to login page (logout button) */
function goToLogin() {
  userLogout();
  window.location.href = "/login";
}


/* --- LOGIN/LOGOUT USER FUNCTIONS --- */

/* LogOUT for every page after user exit*/
/*
window.addEventListener('beforeunload', function() {
    userLogout();
});
/*

/* Log out user every 3 minutes */
setInterval(() => {
  console.log('logout');
    userLogout();
    window.location.href = "/login";
}, 180000); // Every 180 seconds

/* User logout general function */
function userLogout() {
    $.ajax({
      data : {},
      type : 'POST',
      url : '/logout'
      })
      .done(function(data) {
        if(data == 'OK') {
          return;
        }
        else {
          document.getElementById('appimg').textContent = "LOGIN SERVER ERROR";
      }
    });
}
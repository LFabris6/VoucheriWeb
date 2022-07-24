


const firebaseConfig = {
    apiKey: "AIzaSyB0zenvZnCkMVJNRXDrU-oSfSLos56B6iU",
    authDomain: "dron-334213.firebaseapp.com",
    projectId: "dron-334213",
    storageBucket: "dron-334213.appspot.com",
    messagingSenderId: "684334334704",
    appId: "1:684334334704:web:1f11d7e9b5a28318aff835"
  };
  
  
    const app = firebase.initializeApp(firebaseConfig);
    const messaging = firebase.messaging();
    
  
  function getToken() {
      const messaging = firebase.messaging();
  
      messaging.getToken({ vapidKey: 'BIN5ClrbJBohDtmFh45z6ITEc8qpE1fW_sXJvBlILGrycIyfEIA2gIBOBKsIdKriWXo0gz_3C_Eq5Dr79kl0v54' }).then((currentToken) => {
        if (currentToken) {
          console.log(currentToken)
          sendTokenToServer(currentToken)
        } else {
          // Show permission request UI
          console.log('No registration token available. Request permission to generate one.');
          // ...
        }
      }).catch((err) => {
        console.log('An error occurred while retrieving token. ', err);
        // ...
      });
    
    }
  
    
  
  
    function isTokenSentToServer() {
      //if (window.localStorage.getItem('sentToServer') == 1) {
      //    return true;
      //}
      //return false;
      return false;
   }
  
   function setTokenSentToServer(sent) {
    if (sent) {
        window.localStorage.setItem('sentToServer', 1);
    } else {
        window.localStorage.setItem('sentToServer', 0);
    }
  }
  
  
  
  function requestPermission() {
      // [START messaging_request_permission]
      Notification.requestPermission().then((permission) => {
        if (permission === 'granted') {
          console.log('Notification permission granted.');
          getToken();
          // TODO(developer): Retrieve a registration token for use with FCM.
          // ...
        } else {
          console.log('Unable to get permission to notify.');
        }
      });
      // [END messaging_request_permission]
    }
  
  
  
  requestPermission();
  
  
  function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie != '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
              var cookie = jQuery.trim(cookies[i]);
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) == (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }
  
  
  function sendTokenToServer(currentToken) {
      if (!isTokenSentToServer()) {
          console.log('Sending token to server...');
          let access_token = '';
          // TODO(developer): Send the current token to your server.
          fetch('')
          fetch('/api/devices/', {
              method: "POST",
              headers: {
                  'Content-Type': 'application/json',
                  'Authorization': 'Token: ' + getCookie('token'),
                  'X-CSRFToken': getCookie('csrftoken')
              },
              body: JSON.stringify({
                  'registration_id': currentToken,
                  'type': 'web',
              }),
              credentials: "include",
          }).then(function (response) {
              console.log(response);
          })
          setTokenSentToServer(true);
      } else {
          console.log('Token already sent to server so won\'t send it again ' +
              'unless it changes');
      }
  
  }
  
  
  
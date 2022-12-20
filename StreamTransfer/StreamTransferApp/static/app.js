// Include the CSRF token in the AJAX request
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
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
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});


// Define the transferPlaylists() function
function transferPlaylists() {
  // Make an AJAX request to the app's transfer-playlists URL
  $.ajax({
    url: '/playlists/transfer/',
    method: 'POST',
    success: function(data) {
      // Handle the response from the server
      alert(data);
    }
  });
}

// Make an AJAX request to authenticate the user
$(document).ready(function() {
  $.ajax({
    url: '/playlists/authenticate/',
    method: 'POST',
    success: function(response) {
      console.log(response);
    }
  });

  $(document).foundation();
});
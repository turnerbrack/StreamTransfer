const loginButton = document.getElementById("login-button");

loginButton.addEventListener("click", function() {
  // Use the Tidal API to authenticate the user and access their playlists
  tidalAPI.authenticate(function(error, result) {
    if (error) {
      console.log("Error authenticating user:", error);
    } else {
      // Once the user is authenticated, get their playlists
      tidalAPI.getPlaylists(function(error, playlists) {
        if (error) {
          console.log("Error getting playlists:", error);
        } else {
          // Display the playlists in the web page
          const playlistsList = document.createElement("ul");
          playlists.forEach(function(playlist) {
            const playlistItem = document.createElement("li");
            playlistItem.textContent = playlist.name;
            playlistsList.appendChild(playlistItem);
          });
          document.body.appendChild(playlistsList);
        }
      });
    }
  });
});

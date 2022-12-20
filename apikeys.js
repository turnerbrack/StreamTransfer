var tidalapi = require('tidalapi');

var api = new tidalapi({
    username: 'brackturner@gmail.com' ,
    password: '42666181bt',
    token: 'u5qPNNYIbD0S0o36MrAiFZ56K6qMCrCmYPzZuTnV',
    quality: 'HIGH'
});

api.search({type: 'tracks', query: 'Dream Theater', limit: 1}, function(data){
    console.log(data.tracks);
  })
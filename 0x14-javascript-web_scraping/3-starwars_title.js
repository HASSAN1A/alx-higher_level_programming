#!/usr/bin/node
// makes get request for SW movie id
const request = require('request');
request(`http://swapi-api.hbtn.io/api/films/${process.argv[2]}`, function (error, response, body) {
  error && console.log(error);
  console.log(JSON.parse(body).title);
});

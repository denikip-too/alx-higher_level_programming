#!/usr/bin/node
// Js script that prints the title of a Star Wars movie where the episode
// number matches a given integer
let request = require('request');
let url = 'https://swapi-api.hbtn.io/api/films/';
request.get(url + process.argv[2] + '/', function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});

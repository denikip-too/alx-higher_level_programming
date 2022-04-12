#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles”
// is present
let request = require('request');
let url = process.argv[2];
request.get(url + '/18/', function(error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let temp = JSON.parse(body);
    let j = 0;
    for (let i = 0; i < temp.length; i++) {
      j++;
    }
    console.log(j);
  }
});

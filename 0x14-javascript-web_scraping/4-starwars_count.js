#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles”
// is present
const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const temp = JSON.parse(body);
    console.log(temp.reduce((j, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? j + 1
        : j;
    }, 0));
  }
});

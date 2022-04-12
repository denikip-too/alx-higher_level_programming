#!/usr/bin/node
// JS script that gets the contents of a webpage and stores it in a file
let request = require('request');
let fs = require('fs');
let url = process.argv[2];
let file = process.argv[3];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body , function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});

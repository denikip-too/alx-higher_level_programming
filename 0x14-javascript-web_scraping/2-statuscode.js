#!/usr/bin/node
// JS script that display the status code of a GET request
let request = require('request');
let url = process.argv[2]
request(url, (error, status_code) => {
  if (error) {
    console.log(error)
  } else {
    console.log("code: " + status_code.statusCode);
  }
});

#!/usr/bin/node
// JS script that display the status code of a GET request

const request = require('request')
const url = process.argv[2]
request(url, (error, statuscode) => {
  if (error) {
    console.log(error)
  } else {
    console.log('code: ' + statuscode.statusCode)
  }
})

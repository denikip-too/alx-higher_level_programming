#!/usr/bin/node
// JS Script that reads and prints the content of a file
const fs = require('fs');
fs.readFile(process.argv[2], function (error, contents) {
  if (error) {
    console.log(error);
  } else {
    console.log(contents.toString());
  }
});

#!/usr/bin/node
// prints two arguments passed to it

if (!(process.argv[3]) && process.argv[2]) {
  console.log(process.argv[2] + ' is undefined');
} else if (process.argv[2] && process.argv[3]) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else {
  console.log('undefined is undefined');
}

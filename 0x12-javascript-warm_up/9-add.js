#!/usr/bin/node
// prints the addition of 2 integers

function add(a, b) {
  return (a + b);
}
const x = parseInt(process.argv[2]);
const y = parseInt(process.argv[3]);
if (x && y) {
  const result = add(x, y);
  console.log(result);
} else {
  console.log('NaN');
}

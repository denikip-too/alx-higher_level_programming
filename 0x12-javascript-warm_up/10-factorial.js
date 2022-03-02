#!/usr/bin/node
// computes and prints a factorial

function factorial (x) {
  if (x === 0) {
    return (1);
  } else {
    return (x * factorial(x - 1));
  }
}
const y = parseInt(process.argv[2]);
if (y) {
  const result = factorial(y);
  console.log(result);
} else {
  console.log('1');
}

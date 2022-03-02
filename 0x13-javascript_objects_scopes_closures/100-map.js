#!/usr/bin/node
// imports an array and computes a new array
const lst = require('./100-data').list;
console.log(lst);
console.log(lst.map((x, i) => x * i));

#!/usr/bin/node
//prints the addition of 2 integers

function add(a, b) {
	let c = a + b;
	return (c);
}
let x = parseInt(process.argv[2]);
let y = parseInt(process.argv[3]);
if (x && y) {
	let result = add(x, y);
	console.log(result);
}

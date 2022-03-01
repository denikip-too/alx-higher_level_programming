#!/usr/bin/node
//prints square

let x = parseInt(process.argv[2]);
if (x) {
	for (let i = 1; i <= x; i++) {
		console.log('X'.repeat(x));
	}
}
else {
	console.log('Missing size');
}

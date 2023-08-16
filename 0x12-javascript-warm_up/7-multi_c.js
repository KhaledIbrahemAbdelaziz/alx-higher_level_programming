#!/usr/bin/node
const num = process.argv[2];
const parsenum = parseInt(num);
if (isNaN(parsenum)) {
	console.log('Missing number of occurrences');
} else {
	for (let i = 0; i < parsenum; i++) {
		console.log('C is fun');
	}
}

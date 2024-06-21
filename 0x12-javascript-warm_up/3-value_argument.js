#!/usr/bin/node
const count = process.argv;
if (count == process.argv[2]) {
	console.log('No argument');
} else {
	console.log(process.argv[3]);
}

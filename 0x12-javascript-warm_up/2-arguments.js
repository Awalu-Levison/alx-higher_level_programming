#!/usr/bin/node
const myArgs = process.argv;
if (myArgs == process.argv[0]) {
	console.log('No argument');
} else if (myArgs == process.argv[1]) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}

#!/usr/bin/node
const arg_count = process.argv.length;
let message;
if (arg_count == 2) {
	message = 'No argument';
} else if (arg_count == 3) {
	message = 'Argument found';
} else {
	message = 'Arguments found';
}
console.log(message);

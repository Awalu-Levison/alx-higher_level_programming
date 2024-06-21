#!/usr/bin/node
const userArg = process.argv[2];
if (userArg == undefined || userArg == '') {
	console.log('No argument');
} else {
	console.log(userArg);
}

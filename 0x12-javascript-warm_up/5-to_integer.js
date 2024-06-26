#!/usr/bin/node
const UserData = Math.floor(Number(process.argv[2]));
console.log(isNaN(UserData) ? 'Not a number' : `My number: ${UserData}`);

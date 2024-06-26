#!/usr/bin/node

const User_Input = process.argv[2];
const num = Number(User_Input);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ${math.floor(num)}');
}

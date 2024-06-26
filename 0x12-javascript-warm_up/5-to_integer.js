#!/usr/bin/node

const user_data = process.argv[2];
const num = Number(user_data);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Math.floor(num)}`);
}

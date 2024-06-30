#!/usr/bin/node

const x = Math.floor(Number(process.argv[2]));

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let row1 = 0; row1 < x; row1++) {
    let row2 = '';
    for (let i = 0; i < x; i++) row2 += 'X';
    console.log(row2);
  }
}

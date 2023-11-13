#!/usr/bin/node

const argv = process.argv
const num = parseInt(parseFloat(argv[2]));
let i = 0;
let j = 0;

if (isNaN(num)) {
  console.log('Missing size');
} else {
    while (i < num) {
      while (j < num) {
        console.log('X'.repeat(num));
        j++;
      }
      i++;
    }
}

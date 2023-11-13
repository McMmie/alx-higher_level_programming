#!/usr/bin/node

const argv = process.argv;
const num = parseInt(parseFloat(argv[2]));
let i = 0;

if (argv.length < 3 || isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  while (i < num) {
    console.log('C is fun');
    i++;
  }
}

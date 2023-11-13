#!/usr/bin/node
// prints command line arguments
const argv = process.argv;

if (argv.length < 3) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

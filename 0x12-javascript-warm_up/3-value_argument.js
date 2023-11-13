#!/usr/bin/node
const argv = process.argv;
let len = 2;
if (!argv[len]) {
  console.log('No argument');
} else {
  while (argv[len]) {
    console.log(argv[len]);
    len++;
  }
}

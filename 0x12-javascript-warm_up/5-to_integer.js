#!usr/bin/node
const argv = process.argv;
let num = parseInt(parseFloat(argv[2]));
if (!num || num === NaN) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}

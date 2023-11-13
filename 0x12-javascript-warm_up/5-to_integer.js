#!usr/bin/node
const argv = process.argv;
const num = parseInt(parseFloat(argv[2]));
if (!num || num.isnan()) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}

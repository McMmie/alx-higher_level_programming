#!/usr/bin/node
function add(a, b) {

  console.log(parseInt(a) + parseInt(b))
}
const argv = process.argv;
add(argv[2], argv[3]);

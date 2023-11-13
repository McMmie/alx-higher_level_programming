#!/usr/bin/node
const argv = process.argv;
let myArray = [...argv];
if (argv.length < 4) {
  console.log('0');
} else {
  myArray.splice(0, 2)
  myArray.sort(function(a, b) {
    return (b - a);
  });
  console.log(myArray[1]);
}

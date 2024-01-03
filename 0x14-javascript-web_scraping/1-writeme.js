#!/usr/bin/node
// A script that writes a string to a file

const fs = require('fs');
if (process.argv.length !== 4) {
  console.error('Usage: ./script.js <filename> <content>');
  process.exit(1);
}

fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});

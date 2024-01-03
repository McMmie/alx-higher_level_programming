#!/usr/bin/node
// a script that reads and prints the content of a file.

const fs = require('fs');

const filePath = process.argv[1];

// Read file asynchronously
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
    // Now you can use 'data' as the content of the file
  }
});

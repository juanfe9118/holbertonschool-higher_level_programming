#!/usr/bin/node
// Reads and prints the content of a file.
const fs = require('fs');
const fileName = process.argv[2];

fs.readFile(fileName, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

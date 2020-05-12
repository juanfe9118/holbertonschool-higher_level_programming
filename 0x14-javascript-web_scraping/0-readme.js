#!/usr/bin/node
// Reads and prints the content of a file.
const fs = require('fs');
const fileName = process.argv[2];

fs.readFile(fileName, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});

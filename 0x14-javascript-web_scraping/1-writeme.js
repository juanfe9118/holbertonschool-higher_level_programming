#!/usr/bin/node
// Writes a string to a file.
const fs = require('fs');
const fileName = process.argv[2];
const fileText = process.argv[3];

fs.writeFile(fileName, fileText, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});

#!/usr/bin/node
// A script that reads and prints the content of a file

const fs = require('fs');
const file = process.argv[2];
const text = process.argv[3];

fs.writeFile(file, text, 'utf8', (err) => {
  if (err) {
    console.error('Error writing to file:', err);
    return;
  }
});

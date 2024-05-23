#!/usr/bin/node
// A script that writes and prints the content to a file

const fs = require('fs');
const file = process.argv[2];
const text = process.argv[3];

fs.writeFile(file, text, 'utf8', (err) => {
  if (err) {
    console.error('Error writing to file:', err);
  }
});

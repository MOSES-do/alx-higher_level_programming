#!/usr/bin/node
const { argv } = require('process');

let num = +(argv[2]);
if (isNaN(num)) console.log('Missing size');
for (let i=0; i < num; i++) {
  let xed = '';
	for (let j=0; j < num; j++) {
    xed += 'X';
	}
  console.log(xed);
}

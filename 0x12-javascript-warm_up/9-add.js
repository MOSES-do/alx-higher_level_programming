#!/usr/bin/node
const { argv } = require('process');

const a = +(argv[2]);
const b = +(argv[3]);
function add (a, b) {
  console.log(a + b);
}
add(a, b);

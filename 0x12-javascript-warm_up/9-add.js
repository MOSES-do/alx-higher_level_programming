#!/usr/bin/node
const { argv } = require('process');

let a = +(argv[2]);
let b = +(argv[3]);
function add (a, b) {
  console.log(a + b);
}
add(a, b);


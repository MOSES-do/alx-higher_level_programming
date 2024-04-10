#!/usr/bin/node

const { argv } = require('process');

let fac = Number(argv[2]);

if (isNaN(fac)) {
  console.log('1');
  return;
}

function factorial (number){
  if (number <= 1) {
    return 1
  }
  return number * factorial(number - 1);
}

result = factorial(fac);
console.log(result);

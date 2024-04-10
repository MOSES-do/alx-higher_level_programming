#!/usr/bin/node

const { argv } = require('process');

if (argv.length < 3) {
  console.log('0');
}
const arr = [];

for (let i = 2; i < argv.length; i++) {
  let num = +(argv[i]);
  arr.push(num);
}

/*
for (val of arr) {
  console.log(val)
}
*/

if (arr.length === 1) console.log('0');

for (let i = 0; i < arr.length; i++) {
  for (let j = i+1; j < arr.length; j++) {
    let temp = arr[i];
    if (arr[i] > arr[j]) {
      arr[i] = arr[j];
      arr[j] = temp;
    }
  }
}

if (arr.length > 1) {
  console.log(arr[arr.length - 2]);
}

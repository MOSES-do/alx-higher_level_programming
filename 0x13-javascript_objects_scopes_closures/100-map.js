#!/usr/bin/node

const list = require('./100-data').list;

const newList = [];

for (let i = 0; i < list.length; i++) {
  multiplier = i * list[i];
  newList.push(multiplier);
}

console.log(list);
console.log(newList);

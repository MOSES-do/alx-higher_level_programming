#!/usr/bin/node

let counter = 0;
function logMe (item) {
  return function () {
    let curCounter = counter++;
    console.log(`${curCounter}: ${item}`);
  }("");
}

module.exports = {
  logMe
}

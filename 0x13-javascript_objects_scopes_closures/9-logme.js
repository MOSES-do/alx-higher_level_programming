#!/usr/bin/node

let counter = 0;
function logMe (item) {
  return (function () {
    const curCounter = counter++;
    console.log(`${curCounter}: ${item}`);
  })('');
}

module.exports = {
  logMe
};

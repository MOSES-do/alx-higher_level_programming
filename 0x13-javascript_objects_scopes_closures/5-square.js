#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor(size) {
    super();
    if (this.size <= 0) return;
    this.width = size;
    this.height = size;
    this.size = size;
  }
}
module.exports = Square;

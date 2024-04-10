#!/usr/bin/node
const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  constructor(size) {
    super();
    this.size = size;
  }
  
  charPrint(val) {
    if (this.size <= 0) return;
    const stamp = val === undefined ? 'X' : val;
    for (let i = 0; i < this.size; i++) {
      let str = '';
      for (let j = 0; j < this.size; j++) {
        str += stamp;
      }
      console.log(str);
    }
  }

}
module.exports = Square;

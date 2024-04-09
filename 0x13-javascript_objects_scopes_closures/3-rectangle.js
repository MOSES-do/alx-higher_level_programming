#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w === 0 || w < 0 || h === 0 
      || h < 0 || !h || !w) {
      return; 
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    for (let i = 0; i < this.width; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str += 'X';
      }
      console.log(str);
    }
  }
}

module.exports = Rectangle;

#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !h || !w) {
      return 0; 
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str += 'X';
      }
      console.log(str);
    }
  }

  double() {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  rotate() {
    let temp = this.height;
    this.height = this.width;
    this.width = temp;
  }
}
module.exports = Rectangle;

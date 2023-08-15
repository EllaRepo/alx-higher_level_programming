#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    const sqr = c.repeat(this.width);
    for (let i = 0; i < this.width; i++) {
      console.log(sqr);
    }
  }
}

module.exports = Square;

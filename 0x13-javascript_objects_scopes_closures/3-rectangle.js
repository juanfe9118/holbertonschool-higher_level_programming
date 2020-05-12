#!/usr/bin/node
// Rectangle class that has a constructor with height and width
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const p_char = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(p_char.repeat(this.width));
    }
  }
}

module.exports = Rectangle;

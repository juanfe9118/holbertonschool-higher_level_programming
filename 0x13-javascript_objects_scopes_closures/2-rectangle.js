#!/usr/bin/node
// Rectangle class that has a constructor with height and width
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(h) && Number.isInteger(w) && h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    }
  }
}

module.exports = Rectangle;

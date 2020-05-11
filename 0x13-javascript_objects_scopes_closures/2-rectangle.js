#!/usr/bin/node
// Rectangle class that has a constructor with height and width
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.height = h;
      this.width = w;
    }
  }
}

module.exports = Rectangle;

#!/usr/bin/node
// class Square that inherits from Rectangle
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      for (let y = 0; y < this.size; y++) {
        console.log('X'.repeat(this.size));
      }
    } else {
      for (let y = 0; y < this.size; y++) {
        console.log('C'.repeat(this.size));
      }
    }
  }
};

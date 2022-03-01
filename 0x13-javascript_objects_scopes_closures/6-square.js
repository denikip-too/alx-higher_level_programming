#!/usr/bin/node
// class Square that inherits from Rectangle

module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (typeof c === 'undefined') {
      for (let z = 0; z < this.height; z++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      for (let y = 0; y < this.height; y++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
};

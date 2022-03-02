#!/usr/bin/node
// class Square that inherits from Rectangle

module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      for (let y = 0; y < this.height; y++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
};

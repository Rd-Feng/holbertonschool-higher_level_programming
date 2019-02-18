#!/usr/bin/node
class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }
}
Square.prototype.charPrint = function (c = 'X') {
  for (let i = 0; i < this.height; i++) {
    console.log(c.repeat(this.width));
  }
};
module.exports = Square;

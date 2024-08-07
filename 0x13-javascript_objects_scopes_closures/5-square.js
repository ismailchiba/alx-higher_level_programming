#!/usr/bin/node

const Rectangle = require('./4-rectangle');

/**
 * Class Square : parallelogram with 4 angles.
 */

class Square extends Rectangle {
  /**
 * Creates a new Square with the given dimensions.
 * @param {Number} size The value of the width and height.
 */
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;

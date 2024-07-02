#!/user/bin/node

const SquareParent = require('./5-square');

/**
 * Class Square : parallelogram with 4 angles.
 */

class Square extends SquareParent {
  /**
 * Creates a new Square with the given dimensions.
 * @param {Number} size The value of the width and height.
 */
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (c == undefined) {
      // Call a method from the parent class
      super.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        let s = '';
        for (let j = 0; j < this.height; j++) {
          s += c;
        }
        console.log(s);
      }
    }
  }
}

module.exports = Square;

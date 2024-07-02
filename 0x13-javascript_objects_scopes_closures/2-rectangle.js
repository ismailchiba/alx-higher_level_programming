#!/user/bin/node
/**
 * Class Rectangle : parallelogram with 4 angles.
 */

class Rectangle {
  constructor (w, h) {
    /**
         * Create a Rectangle with known width and height.
         * @param {number} w the value of the width.
         * @param {number} h the value of the height.
         * */
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;

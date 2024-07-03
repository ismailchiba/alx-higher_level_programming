#!/usr/bin/node
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

  print () {
    // Loop through each row
    for (let i = 0; i < this.height; i++) {
      // Create a row of 'width' number of 'X'
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;

#!/usr/bin/node
function Square (num, txt) {
  if (Number.isNaN(num)) {
    console.log('Missing size');
  } else if (num >= 0) {
    for (let i = 0; i < num; i++) {
      console.log(txt.repeat(num));
    }
  }
}

Square(Number.parseInt(process.argv[2]), 'X');

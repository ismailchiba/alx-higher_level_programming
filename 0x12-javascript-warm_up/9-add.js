#!/usr/bin/node
function add (num0, num1) {
  if (Number.isNaN(num0) || Number.isNaN(num1)) {
    console.log('NaN');
  } else {
    console.log(num0 + num1);
  }
}

add(Number.parseInt(process.argv[2]), Number.parseInt(process.argv[3]));

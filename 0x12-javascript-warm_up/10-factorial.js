#!/usr/bin/node
function factorial (num) {
  if (Number.isNaN(num) || (num <= 0)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(Number.parseInt(process.argv[2])));

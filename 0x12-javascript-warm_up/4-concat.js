#!/usr/bin/node
const arg0 = process.argv[2];
const arg1 = process.argv[3];

console.log((arg0 !== undefined ? arg0 : 'undefined') + ' is ' + (arg1 !== undefined ? arg1 : 'undefined'));

#!/user/bin/node
let num = 0;
/**
 * Print {num} the number of arguments already printed
 * beside the new argument value
 * @param {String} item The message to be logged.
 *
 */

exports.logMe = function (item) {
  console.log(num + ': ' + item);
  num++;
};

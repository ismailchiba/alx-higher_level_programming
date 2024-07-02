#!/user/bin/node
/**
 * Reverses an array.
 * @param {Array} list the array to a reverse
 * @return The reversed array
 */
exports.esrever = function (list) {
  const n = list.length;
  const newList = new Array(n);

  list.forEach((item, i) => {
    newList[n - i - 1] = item;
  });
  return newList;
};

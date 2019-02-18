#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  list.forEach(e => {
    if (e === searchElement) {
      i++;
    }
  });
  return i;
};

#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (let i = 0; i < list.length; i++) {
    let item = list[i];

    if (item === searchElement) {
      count += 1;
    }
  }
  return count;
}

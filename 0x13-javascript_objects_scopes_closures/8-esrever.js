#!/usr/bin/node

exports.esrever = function(list) {
  let length = Math.floor(list.length / 2);

  for (let i = 0; i < length; i++) {
    let temp = list[i];
    list[i] = list[list.length - i - 1];
    list[list.length - i - 1] = temp;
  }

  return list;
}

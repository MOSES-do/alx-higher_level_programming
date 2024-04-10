#!/usr/bin/node

exports.esrever = function (list) {
  const length = Math.floor(list.length / 2);

  for (let i = 0; i < length; i++) {
    const temp = list[i];
    list[i] = list[list.length - i - 1];
    list[list.length - i - 1] = temp;
  }

  return list;
};

#!/usr/bin/node
// prints the number of arguments already printed and the new argument value

exports.logMe = function (item) {
  let count = 0;
  console.log(count + ': ' + item);
  count++;
};

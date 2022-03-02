#!/usr/bin/node
/* imports a dictionary of occurrences by user id and computes a dictionary of user
ids by occurrence
- A key is a number of occurrences
- A value is the list of user ids
*/
const dct = require('./101-data.js').dict;
const newDict = {};
for (const key in dct) {
  if (newDict[dct[key]] === undefined) {
    newDict[dct[key]] = [];
  }
  newDict[dct[key]].push(key);
}
console.log(newDict);

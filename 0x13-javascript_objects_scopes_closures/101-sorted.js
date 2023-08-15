#!/usr/bin/node
const dict = require('./101-data.js').dict;

const newDict = {};
for (const id in dict) {
  const key = dict[id];
  if (!newDict[key]) {
    newDict[key] = [];
  }
  newDict[key].push(id);
}
console.log(newDict);

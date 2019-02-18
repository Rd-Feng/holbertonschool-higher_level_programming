#!/usr/bin/node
const dict = require('./101-data').dict;
const s = {};
for (let k in dict) {
  if (s[dict[k]] === undefined) {
    s[dict[k]] = [k];
  } else {
    s[dict[k]].push(k);
  }
}
console.log(s);

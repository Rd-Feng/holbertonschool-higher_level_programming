#!/usr/bin/node
const origin = require('./100-data').list;
const newl = origin.map((e, idx) => e * idx);
console.log(origin);
console.log(newl);

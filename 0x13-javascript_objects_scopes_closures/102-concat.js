#!/usr/bin/node
const fs = require('fs');
let str = fs.readFileSync(process.argv[2], 'utf8');
str += fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], str);

#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request({ url: process.argv[2], methods: 'GET' }, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[3], body, err => {
      if (err) {
        console.log(err);
      }
    });
  }
});

#!/usr/bin/node
const request = require('request');
request({ url: process.argv[2], methods: 'GET' }, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', response && response.statusCode);
  }
});

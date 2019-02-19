#!/usr/bin/node
const request = require('request');
const req = {
  url: process.argv[2],
  method: 'GET'
};
request(req, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    body = JSON.parse(body);
    const s = {};
    body.forEach(task => {
      if (task.completed === true) {
        if (s[task.userId] === undefined) {
          s[task.userId] = 1;
        } else {
          s[task.userId]++;
        }
      }
    });
    console.log(s);
  }
});

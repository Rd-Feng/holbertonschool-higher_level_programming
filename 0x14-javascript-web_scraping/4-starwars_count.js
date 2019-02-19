#!/usr/bin/node
const request = require('request');
let endPoint = 'https://swapi.co/api/people/18/';
request({ url: endPoint, methods: 'GET' }, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(body && JSON.parse(body).films.length);
  }
});

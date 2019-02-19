#!/usr/bin/node
const request = require('request');
const character = 'https://swapi.co/api/people/18/';
request.get(process.argv[2], function (err, response, body) {
  if (err) {
    throw err;
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (let film of films) {
      for (let char of film.characters) {
        if (char === character) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Error:', response.statusCode);
  }
});
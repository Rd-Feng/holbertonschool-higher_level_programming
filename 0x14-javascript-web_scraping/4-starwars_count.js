#!/usr/bin/node
const request = require('request');
const character = 'https://swapi.co/api/people/18/';
if (process.argv[2] !== undefined) {
  request({ url: process.argv[2], methods: 'GET' }, function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      const films = JSON.parse(body).results;
      let count = 0;
      films.forEach(film => {
        if (film.characters.includes(character)) {
          count++;
        }
      });
      console.log(count);
    }
  });
}

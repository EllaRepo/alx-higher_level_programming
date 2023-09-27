#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
let movieId = parseInt(process.argv[2], 10);
let characters = [];

request(url, function (err, response, body) {
  if (err == null) {
    const results = JSON.parse(body).results;
    if (movieId < 4) {
      movieId += 3;
    } else {
      movieId -= 3;
    }
    for (let i = 0; i < results.length; i++) {
      if (results[i].episode_id === movieId) {
        characters = results[i].characters;
        break;
      }
    }
    for (let j = 0; j < characters.length; j++) {
      request(characters[j], function (err, response, body) {
        if (err == null) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});

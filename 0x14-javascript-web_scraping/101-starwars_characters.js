#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
let movieId = parseInt(process.argv[2], 10);
let characters = [];

request(url, (error, response, body) => {
  if (error == null) {
    if (movieId < 4) {
      movieId += 3;
    } else if (movieId < 7) {
      movieId -= 3;
    }
    const results = JSON.parse(body).results;
    for (let i = 0; i < results.length; i++) {
      if (results[i].episode_id === movieId) {
        characters = results[i].characters;
        break;
      }
    }
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], function (err, response, body) {
        if (err == null) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});

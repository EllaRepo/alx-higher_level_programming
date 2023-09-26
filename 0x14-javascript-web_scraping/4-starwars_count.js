#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error == null) {
    const films = JSON.parse(body).results;
    const wedgeAntillesFilms = films.filter((film) => {
      const characters = film.characters;
      return characters.search('18');
    });
    console.log(wedgeAntillesFilms.length);
  }
});

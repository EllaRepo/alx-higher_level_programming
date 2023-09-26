#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, (error, response, body) => {
  if (error == null) {
    const films = JSON.parse(body).results;
    for (let i = 0; i < films.length; i++) {
      const characters = films[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].search('18') > 0) {
          count++;
        }
      }
    }
    console.log(count);
  }
});

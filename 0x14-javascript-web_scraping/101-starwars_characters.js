#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (error == null) {
    const characters = JSON.parse(body);
    printCharacterNames(characters, 0);
  }
});

function printCharacterNames (characters, i) {
  request(characters[i], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (i + 1 < characters.length) {
        printCharacterNames(characters, i + 1);
      }
    }
  });
}

printCharacterNames(process.argv[2]);

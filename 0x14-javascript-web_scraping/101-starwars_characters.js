#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (error == null) {
    const characters = JSON.parse(body);
    printCharacterNamesSync(characters, 0);
  }
});

function printCharacterNamesSync (characters, i) {
  request(characters[i], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (i + 1 < characters.length) {
        printCharacterNamesSync(characters, i + 1);
      }
    }
  });
}

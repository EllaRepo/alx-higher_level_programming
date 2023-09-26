#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url).on('response', function (error, response) {
  if (error == null) {
    console.log('code: ' + response.statusCode);
  }
});

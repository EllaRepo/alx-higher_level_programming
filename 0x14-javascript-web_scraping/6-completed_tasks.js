#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error == null) {
    const todos = JSON.parse(body);
    const completedTodosByUser = todos.reduce((result, todo) => {
      if (todo.completed) {
        const userId = todo.userId;
        if (!result[userId]) {
          result[userId] = 0;
        }
        result[userId]++;
      }
      return result;
    }, {});

    console.log(completedTodosByUser);
  }
});

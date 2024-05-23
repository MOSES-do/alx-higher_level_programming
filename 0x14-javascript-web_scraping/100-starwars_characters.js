#!/usr/bin/node
// script that creates an object with userid:total_no_of_tasks_done

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

const fetchTodo = () => {
  request(url, { json: true }, (error, response, body) => {
    if (error) console.log(error);
    const result = body.characters;
    for (const uri of result) {
      request(uri, { json: true }, (error, response, body) => {
        if (error) console.log(error);
        const character = body.name;
        console.log(character);
      });
    }
  });
};
fetchTodo();

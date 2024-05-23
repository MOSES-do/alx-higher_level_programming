#!/usr/bin/node
// A script that retrieves values based on a given integer

const request = require('request');
const id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, { json: true }, (error, response, body) => {
  if (error) console.log(error);
  console.log(body.title);
});

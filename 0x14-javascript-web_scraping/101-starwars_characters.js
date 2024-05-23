#!/usr/bin/node
// script that returns actors from a movie according to api listing

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

const fetchMovieStars = () => {
  request(url, { json: true }, (error, response, body) => {
    if (error) console.log(error);
    const result = body.characters;
    for (const uri of result) {
      request(uri, { json: true }, (error, response, body) => {
        console.log(uri);
        if (error) console.log(error);
        const character = body.name;
        console.log(character);
      });
    }
  });
};
fetchMovieStars();

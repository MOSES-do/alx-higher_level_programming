#!/usr/bin/node
// A script that retrieves values based on a given integer

const request = require('request');
const url = process.argv[2];

const fetchMovies = () => {
  const chars = [];
  let count = 0;
  request(url, { json: true }, (error, response, body) => {
    if (error) console.log(error);
    const result = body.results;
    for (const movie of result) {
      chars.push(movie.characters);
    }

    for (const arr of chars) {
      for (const url of arr) {
        if (url.includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  });
};

fetchMovies();

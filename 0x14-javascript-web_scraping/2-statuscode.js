#!/usr/bin/node
// A script to return the status of a get request

function fetchAlx () {
  const request = require('request');
  const url = process.argv[2];

  request(url, (error, response) => {
    if (error) console.log(error);
    console.log('code:', response.statusCode);
  });
}
fetchAlx();

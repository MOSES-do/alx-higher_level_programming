#!/usr/bin/node
// A script that retrieves values based on a given integer

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];

const scrapWeb = () => {
  request(url, { json: true }, (error, response, body) => {
    if (error) console.log(error);

    fs.writeFile(fileName, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  });
};

scrapWeb();

#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
    (err, response, body) => {
      if (err) { console.log(err); }
      console.log(JSON.parse(body).title);
    });
}

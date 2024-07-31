#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const charId = '18';

  request(process.argv[2], (err, res, body) => {
    if (err) {
      console.log(err);
    }
    const Data = JSON.parse(body);
    const films = Data.results;
    const count = films.filter(film =>
      film.characters.some(character => character.endsWith(`/${charId}/`))
    ).length;
    console.log(count);
  });
}

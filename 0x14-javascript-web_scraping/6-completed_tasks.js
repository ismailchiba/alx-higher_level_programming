#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  request(process.argv[2], (err, res, body) => {
    const total = {};
    if (err) {
      console.log(err);
    }
    try {
      const tasks = JSON.parse(body);

      tasks.forEach(element => {
        if (element.completed) {
          if (!total[element.userId]) {
            total[element.userId] = 0;
          }
          total[element.userId]++;
        }
      });
      console.log(total);
    } catch (parseError) {
      console.error(`Failed to parse JSON response: ${parseError}`);
    }
    // const todos = Data.results;
  });
}

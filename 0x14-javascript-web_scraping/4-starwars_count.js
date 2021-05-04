#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    for (const result of data.results) {
      for (const character of result.characters) {
        if (character.endsWith('/18/')) {
          count += 1;
        }
      }
    }
  }
  console.log(count);
});

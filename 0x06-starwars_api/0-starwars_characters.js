#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const filmsApiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(filmsApiUrl, async function (err, res, body) {
  if (err) {
    return console.log(err);
  } else {
    const characterUrls = JSON.parse(body).characters;
    for (const characterUrl of characterUrls) {
      const characterData = await new Promise((resolve, reject) => {
        request(characterUrl, (err, res, body) => {
          if (err) {
            reject(err);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
      console.log(characterData);
    }
  }
});

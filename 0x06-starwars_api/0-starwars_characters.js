#!/usr/bin/node
/* Script that prints all characters of a Star Wars movie */
const request = require('request');

// checks if the correct number of arguments (2) is provided
if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const filmsApiUrl = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];

// Function to fetch data from a given URL and return a Promise 
function fetchData(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

// function to fetch and print Star Wars characters from a specified movie
async function printStarWarsCharacters() {
  try {
    const filmData = await fetchData(`${filmsApiUrl}${movieId}/`);
    const characterUrls = filmData.characters;

    for (const characterUrl of characterUrls) {
      try {
        const characterData = await fetchData(characterUrl);
        console.log(characterData.name);
      } catch (error) {
        console.error(`Error fetching character data: ${error.message}`);
      }
    }
  } catch (error) {
    console.error(`Error fetching film data: ${error.message}`);
    process.exit(1); // Exit with a non-zero status code on error
  }
}

printStarWarsCharacters();
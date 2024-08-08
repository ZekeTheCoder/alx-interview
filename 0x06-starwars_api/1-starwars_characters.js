#!/usr/bin/node
/**
 * Script that prints all characters of a Star Wars movie
 */

const request = require('request');

// checks if the correct number of arguments (2) is provided
if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// URL for the Star Wars films API
const filmsApiUrl = 'https://swapi-api.hbtn.io/api/films/';
// Get the movie ID from command-line arguments
const movieId = process.argv[2];

/**
 * Function to fetch data from a given URL and return a Promise
 */
function fetchData(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error); // Reject the Promise if there is an error
      } else {
        resolve(JSON.parse(body)); // Resolve the Promise with parsed JSON data
      }
    });
  });
}

/**
 * Main function to fetch and print Star Wars characters from a specified movie
 */
async function printStarWarsCharacters() {
  try {
    // Fetch film data for the given movie ID
    const filmData = await fetchData(`${filmsApiUrl}${movieId}/`);
    const characterUrls = filmData.characters; // Get the list of character URLs

    // Iterate over each character URL and fetch character data
    for (const characterUrl of characterUrls) {
      try {
        // Fetch character data and print the character name
        const characterData = await fetchData(characterUrl);
        console.log(characterData.name);
      } catch (error) {
        // Handle errors for fetching character data
        console.error(`Error fetching character data: ${error.message}`);
      }
    }
  } catch (error) {
    // Handle errors for fetching film data
    console.error(`Error fetching film data: ${error.message}`);
    process.exit(1); // Exit with a non-zero status code on error
  }
}

// Call the main function
printStarWarsCharacters();

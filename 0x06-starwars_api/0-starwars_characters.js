#!/usr/bin/node
// Script that prints all characters of a Star Wars movie
 
const filmsApiUrl = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];

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

async function printStarWarsCharacters() {
  try {
    const filmData = await fetchData(`${filmsApiUrl}${movieId}/`);
    const characterUrls = filmData.characters; // Get the list of character URLs

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

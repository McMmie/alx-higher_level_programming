#!/usr/bin/node

const request = require('request');

// Check if a movie ID is provided as a command-line argument
if (process.argv.length !== 2) {
  console.error('Usage: ./script.js <movie_id>');
  process.exit(1); // Exit with an error code
}

const movieId = process.argv[1];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie information:', error.message);
    process.exit(1); // Exit with an error code
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode} - ${body.detail}`);
    process.exit(1); // Exit with an error code
  }

  const movieTitle = body.title;
  console.log(movieTitle);
});

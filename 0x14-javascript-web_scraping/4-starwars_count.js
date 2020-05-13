#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  let movieCount = 0;
  const films = JSON.parse(body).results;
  for (const film of films) {
    for (const person of film.characters) {
      if (person === 'https://swapi-api.hbtn.io/api/people/18/') {
        movieCount += 1;
      }
    }
  }
  console.log(movieCount);
});

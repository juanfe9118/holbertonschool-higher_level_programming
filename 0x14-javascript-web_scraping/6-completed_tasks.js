#!/usr/bin/node
// Computes the number of tasks completed by user id.
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const todoDict = JSON.parse(body);
  const compDict = {};
  for (const task of todoDict) {
    if (task.completed) {
      if (compDict[task.userId]) {
        compDict[task.userId] += 1;
      } else {
        compDict[task.userId] = 1;
      }
    }
  }
  console.log(compDict);
});

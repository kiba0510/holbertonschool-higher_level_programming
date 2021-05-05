#!/usr/bin/nodejs
// Gets the contents of a webpage and stores it in a file.
const request = require('request');
const fs = require('fs');
request(process.argv[2], (error, response, body) => {
  if (error) throw error;
  else {
    fs.writeFile(process.argv[3], body, 'utf8', (error) => {
      if (error) throw error;
    });
  }
});

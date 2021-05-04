#!/usr/bin/nodejs
/*
- Script that display the status code of a GET request
*/
const request = require('request');
const info = {
  url: process.argv[2],
  method: 'GET'
};
request(info, (err, response) => {
  if (err) throw err;
  console.log('code:', response.statusCode);
});

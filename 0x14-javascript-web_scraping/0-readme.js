#!/usr/bin/nodejs
/*
- Read and prints the content of a README file
- fs module: File System
*/
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) throw err;
  else process.stdout.write(data);
});

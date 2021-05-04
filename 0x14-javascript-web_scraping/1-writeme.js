#!/usr/bin/nodejs
/*
- Script that writes a string to a file.
- fs module: File System.
*/
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  if (err) throw err;
});

#!/usr/bin/node

/* script that searches the second
biggest integer in the list of arguments */
const myArray = process.argv.slice(2);

if (myArray.length <= 1) {
  console.log('0');
} else {
  myArray.sort((a, b) => a - b);
  const len = myArray.length;
  console.log(myArray[len - 2]);
}

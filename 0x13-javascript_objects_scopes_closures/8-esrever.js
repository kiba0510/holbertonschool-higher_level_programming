#!/usr/bin/node

// Function that returns the reversed version of a list
exports.esrever = function (list) {
    let myList = [];
    for (let i = list.length - 1; i >= 0; i--) {
        myList.push(list[i]);
    }
    return (myList);
}
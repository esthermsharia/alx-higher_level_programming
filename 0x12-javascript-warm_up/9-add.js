#!/usr/bin/node
/* prints the addition of 2 integers
The first argument is the first integer
The second argument is the second integer
*/

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

console.log(add(process.argv[2], process.argv[3]));

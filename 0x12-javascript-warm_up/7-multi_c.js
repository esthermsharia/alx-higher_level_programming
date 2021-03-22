#!/usr/bin/node
/* prints x times “C is fun”
Where x is the first argument of the script
If the first argument can’t be converted to an integer,
print “Missing number of occurrences”
*/

const lang = 'C is fun';

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(lang);
  }
}

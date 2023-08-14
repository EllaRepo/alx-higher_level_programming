#!/usr/bin/node
const args = process.argv.slice(2);
let msg = '';

if (args.length === 0) {
  msg = 'No argument';
} else if (args.length === 1) {
  msg = 'Argument found';
} else {
  msg = 'Arguments found';
}

console.log(msg);

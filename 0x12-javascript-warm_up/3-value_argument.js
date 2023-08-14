#!/usr/bin/node
const args = process.argv.slice(2);
let msg = '';

if (args.length === 0) {
  msg = 'No argument';
} else {
  msg = args[0];
}

console.log(msg);

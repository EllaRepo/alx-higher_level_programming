#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const nums = args.map(arg => parseInt(arg));
  const sorted = nums.sort((a, b) => b - a);
  console.log(sorted[1]);
}

#!/usr/bin/node
const fs = require('fs');

const srcFile1 = process.argv[2];
const srcFile2 = process.argv[3];
const destFile = process.argv[4];

const concatFile = fs.readFileSync(srcFile1, 'utf8') + fs.readFileSync(srcFile2, 'utf8');

fs.writeFileSync(destFile, concatFile);

#!/usr/bin/node
const process = require('node:process');
const argv = process.argv;

if (argv[2] === undefined) {
	console.log('No argument');
}
else if (argv.length === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}

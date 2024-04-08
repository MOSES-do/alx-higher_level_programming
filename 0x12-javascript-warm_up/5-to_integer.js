#!/usr/bin/node

const { argv } = require('process')
let num = +(argv[2])

if (isNaN(num)) {
	console.log('Not a number')
}
else {
	console.log(`My number: ${num}`)
}

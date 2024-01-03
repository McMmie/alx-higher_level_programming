#!/usr/bin/node
//displays the status code of a GET request

const request = require('request')

if (process.argv.length !== 3) {
	    console.error('Usage: ./script.js <url>');

request(process.argv[2])
.on('response', function(response) {
    console.log('code: ' + response.statusCode); // <--- Here 200
});
.on("error", function(err) {
    console.log( err);
});

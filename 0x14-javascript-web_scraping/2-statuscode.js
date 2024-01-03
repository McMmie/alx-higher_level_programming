#!/usr/bin/node
//displays the status code of a GET request

const request = require('request')

request(process.argv[2])
.on('response', function(response) {
    console.log('code: ', response.statusCode) // <--- Here 200
})
.on("error", function(err){
    console.log("Problem reaching URL: ", err);
 });

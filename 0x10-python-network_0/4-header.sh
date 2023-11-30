#!/bin/bash
#sends a GET request to the URL, and displays the body of the response
curl -F "X-School-User-Id=98" -lX GET $1

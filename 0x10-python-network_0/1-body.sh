#!/bin/bash
# Display the response of the request body
echo $(curl -s -o response_body.txt "$1")

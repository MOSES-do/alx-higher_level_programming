#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
curl -sIL GET http://0.0.0.0:5000/catch_me | grep -q "HTTP/1.1 405 METHOD NOT ALLOWED" && echo "You got me!"

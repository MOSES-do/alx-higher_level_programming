#!/bin/bash
# Display the response of the request body
curl -sIL "$1" | grep -q "HTTP/1.1 200 OK" && curl -sL "$1"

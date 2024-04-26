#!/bin/bash
# Script to send a request url ad display the size of the body response
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'

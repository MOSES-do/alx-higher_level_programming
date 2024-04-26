#!/usr/bin/env bash
# Script to send a request url ad display the size of the body response

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

response_bodysize=$(curl -s -o /dev/null -w "%{size_download}" "$url")

# Display the size of the response body
echo "$response_bodysize"

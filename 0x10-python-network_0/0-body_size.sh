#!/usr/bin/env bash
# Script to send a request url ad display the size of the body response
echo $(curl -s -o /dev/null -w "%{size_download}" "$url")

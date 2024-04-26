#!/bin/bash
# Send a json file to server
curl -X POST -H "Content-Type: application/json" -d @"$2" "$1"

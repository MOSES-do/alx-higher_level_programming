#!/usr/bin/bash
curl -X POST -H "Content-Type: application/json" -d @"$2" "$1"

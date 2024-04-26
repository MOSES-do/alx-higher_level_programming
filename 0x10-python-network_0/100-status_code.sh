#!/bin/bash
# Print status code without usin g pipe or redirection
curl -s -o /dev/null -w "%{http_code}" "$1"

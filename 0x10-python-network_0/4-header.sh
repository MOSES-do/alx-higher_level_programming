#!/bin/bash
# POST request to url and display the body of the response
curl -s -X GET -H "X-School-User-Id: 98" "$1"

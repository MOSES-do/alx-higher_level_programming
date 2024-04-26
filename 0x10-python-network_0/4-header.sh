#!/bin/bash
# POST request to url and display the body of the response
#curl -sIL -X POST -d '{X-School-User-Id:98}' "$1"
curl -H "X-School-User-Id: 98" "$1"


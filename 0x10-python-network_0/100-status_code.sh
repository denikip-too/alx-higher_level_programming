#!/bin/bash
# sends request to URL passed as an argument, displays status code of response
curl -o /dev/null -s -w "%{http_code}" "$1"

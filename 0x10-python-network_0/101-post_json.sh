#!/bin/bash
# sends JSON POST request to URL passed as first argument and display response
curl -sX POST -H "Content-Type: application/json" -H "Accept: application/json" -d "@$2" "$1"

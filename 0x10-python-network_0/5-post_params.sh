#!/bin/bash
# takes URL, sends a POST request to passed URL, and displays body of response
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"

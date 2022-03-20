#!/bin/bash
# takes in URL, sends a request to that URL, and displays size of the response
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2

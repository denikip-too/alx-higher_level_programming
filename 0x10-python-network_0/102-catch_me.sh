#!/bin/bash
# makes a request that causes the server to respond with a message
curl -siH "Accept: You got me!" 0.0.0.0:5000/catch_me

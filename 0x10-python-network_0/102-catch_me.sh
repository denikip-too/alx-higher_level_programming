#!/bin/bash
# makes a request that causes the server to respond with a message
curl -sLX PUT -d "user_id=98" -H "Origin: You got me!" 0.0.0.0:5000/catch_me

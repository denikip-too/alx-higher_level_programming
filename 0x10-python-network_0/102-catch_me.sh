#!/bin/bash
# makes a request that causes the server to respond with a message
curl -sL -X PUT -d user_id=98 -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me

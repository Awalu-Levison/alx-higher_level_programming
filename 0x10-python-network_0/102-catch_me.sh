#!/bin/bash
# A Bash script that makes a request to 0.0.0.0:5000/catch_me, display text of "You got me!"
curl -s -L -X PUT -H "HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me

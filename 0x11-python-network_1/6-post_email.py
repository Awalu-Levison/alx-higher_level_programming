#!/usr/bin/python3
"""
POST an email #1
Write a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
The email must be sent in the variable email
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to error check arguments passed to the script (number or type)
"""

import sys
import requests


if __name__ == "__main__":
    user_req = sys.argv[1]
    email = {'email:' sys.argv[2]}
    req = requests.post(user_req, data=email)
    print(req.email)

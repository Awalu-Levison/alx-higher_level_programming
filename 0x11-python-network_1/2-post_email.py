#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email,
sends a POST request  to the passed URL with the email as
a parameter, and displays the body of the response (decoded in utf-8)
The email must be sent in the email variable
You must use the packages urllib and sys
You are not allowed to import packages other than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
"""


import urllib.request
from sys import argv
import urllib.parse


if __name__ == '__main__':
    url = argv[1]
    email_info = {'email': argv[2]}

    data = urllib.parse.urlencode(email_info)
    data = data.encode('ascii')
    user_req = urllib.request.Request(url, data)

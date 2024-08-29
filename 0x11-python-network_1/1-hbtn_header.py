#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request
to URL displays the value of the X-Request-Id variable
found in the header of the response.
You must use the packages urllib and sys
You are not allow to import packages other than urllib and sys
The value of this variable is different for each request
You don’t need to check arguments passed
to the script (number or type)
You must use a with statement
"""

import sys
from urllib.request import Request, urlopen


if __name__ == '__main__':
    user_url = sys.argv[1]
    user_req = Request(user_url)
    with urlopen(user_req)as response:
        print(dict(response.headers).get('X-Request-Id'))

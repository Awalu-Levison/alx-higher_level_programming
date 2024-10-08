#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8).
You have to manage urllib.error.HTTPError exceptions
and print: Error code: followed by the HTTP status code
You must use the packages urllib and sys
You are not allowed to import other packages than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
"""

import urllib.request
from sys import argv
import urllib.parse


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode())
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))

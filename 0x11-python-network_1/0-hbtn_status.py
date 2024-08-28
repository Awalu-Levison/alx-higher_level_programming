#!/usr/bin/python3
"""Fetching datya using the urllib package in python"""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as user_res:
    html = user_response.read()
    print('Body response:')
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(type(html)))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))

#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)."""
import urllib.error
import urllib.request
from sys import argv


if __name__ == '__main__':
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as r:
            page = r.read()
            print(page.decode('utf8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')

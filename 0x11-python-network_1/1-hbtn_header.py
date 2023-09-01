#!/usr/bin/python3
"""takes in a URL
sends a request to the URL and
displays the value of the X-Request-Id variable
found in the header of the response."""
import urllib.request
import sys

if __name__ == "__main__":
    _Url = sys.argv[1]
    with urllib.request.urlopen(_Url) as res:
        print(dict(res.headers).get("X-Request-Id"))

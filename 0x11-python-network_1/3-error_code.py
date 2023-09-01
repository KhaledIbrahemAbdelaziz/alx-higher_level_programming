#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)."""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    _Url = sys.argv[1]
    req = urllib.request.Request(_Url)
    try:
        with urllib.request.urlopen(req) as res:
            data = res.read()
            print(data.decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

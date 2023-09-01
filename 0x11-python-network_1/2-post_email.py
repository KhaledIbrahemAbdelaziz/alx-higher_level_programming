#!/usr/bin/python3
"""takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    _Url = sys.argv[1]
    url_parsing = {'email' : sys.argv[2]}
    email = urllib.parse.urlencode(url_parsing)
    emails = email.encode('ascii')
    
    req = urllib.request.Request(_Url, emails)
    with urllib.request.urlopen(req) as res:
        data = res.read()
        print(data.decode("utf-8"))

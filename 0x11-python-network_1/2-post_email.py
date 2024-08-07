#!/usr/bin/python3
"""A script that
that takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter,
and displays the body of the response (decoded in utf-8).
"""
if __name__ == "__main__":
    import urllib.request as request
    import urllib.parse as parse
    import sys
    if (sys.argv[2]):
        URL = sys.argv[1]
        key_value = {
            "email": sys.argv[2]
        }
        data = parse.urlencode(key_value).encode("utf-8")
        req = request.Request(URL, data)
        with request.urlopen(req) as resp:
            print(resp.read().decode("utf-8"))

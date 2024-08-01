#!/usr/bin/python3
"""A script that
fetches the URL givin as argument.
"""
if __name__ == "__main__":
    import urllib.request as request
    import sys
    if (sys.argv[1]):
        URL = sys.argv[1]
        req = request.Request(URL)
        with request.urlopen(req) as resp:
            print(dict(resp.headers).get("X-Request-Id"))

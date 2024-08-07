#!/usr/bin/python3
"""A script that
that takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter,
and displays the body of the response (decoded in utf-8).
"""
if __name__ == "__main__":
    import urllib.request as request
    import urllib.error as err
    import sys
    if (sys.argv[1]):
        try:
            URL = sys.argv[1]
            req = request.Request(URL)
            with request.urlopen(req) as resp:
                print(resp.read().decode("utf-8"))
        except err.HTTPError as e:
            print("Error code:", e.code)

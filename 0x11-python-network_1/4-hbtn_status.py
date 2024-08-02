#!/usr/bin/python3
"""A script that
that takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter,
and displays the body of the response (decoded in utf-8).
"""
if __name__ == "__main__":
    import requests
    URL = "https://alx-intranet.hbtn.io/status"
    req = requests.get(URL)
    print("Body response:")
    print(f"\t- type: {type(req.text)}")
    print(f"\t- content: {req.text}")

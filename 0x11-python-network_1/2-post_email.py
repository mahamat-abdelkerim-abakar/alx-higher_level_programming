#!/usr/bin/python3
<<<<<<< HEAD
"""Sends a POST request to a given URL with a given email.

Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
=======
""" Script that takes in a URL and an email, sends a POST request
 And displays the body of the response
"""

>>>>>>> 822dd0bfabd8921df412878fcde8e70da9d11087
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
<<<<<<< HEAD
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
=======
    with urllib.request.urlopen(request) as resp:
        print(resp.read().decode("utf-8"))
>>>>>>> 822dd0bfabd8921df412878fcde8e70da9d11087

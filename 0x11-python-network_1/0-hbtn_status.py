#!/usr/bin/python3
"""display my status"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        f = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(r.text)))
        print("\t-content: {}".format(f.text))

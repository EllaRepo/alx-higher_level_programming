#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status')
    r = response.text
    print("Body response:\n\t- type: {}\n\t- content: {}".format(type(r), r))

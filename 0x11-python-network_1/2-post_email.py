#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST to the requested
URL with the email as the parameter and displays the response
author-omidoyin
"""

from urllib import request, parse
import sys


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))

#!/usr/bin/python3
"""Takes my Github creds (username & password)
and uses the Github API to display my ID
author-omidoyin
"""

from requests import get, auth
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    password = sys.argv[2]
    r = get(url, auth=auth.HTTPBasicAuth(user, password))
    print(r.json().get('id'))

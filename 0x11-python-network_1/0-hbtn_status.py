#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        html = r.read()
        print(f'Body response:\n\t- type: {type(html)}\n\t- content: {html}')
        print(f'\t- utf8 content: {html.decode("utf8")}')

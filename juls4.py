import warnings

import requests

data = []

websites = ['http://google.com', 'http://bbc.co.uk', 'http://seoscanners.net']
for w in websites:
    try:
        r = requests.get(w, timeout=5)
        print(r.reason)
        data.append((r.url, len(r.content), r.elapsed.total_seconds(), str([(l.status_code, l.url) for l in r.history]),
                     str(r.headers.items()), str(r.cookies.items())))
        if str(r.reason) == True or str(r.reason) == True:
            print(r.url)

            warnings.filterwarnings('ignore')
            warnings.warn('DelftStack')
            warnings.warn('Do not show this message')
    except:

        print("Hola")
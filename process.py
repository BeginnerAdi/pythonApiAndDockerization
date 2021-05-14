import requests

url = 'http://localhost:5000/'
myobj = """2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000"""

x = requests.post(url, data = myobj)

print(x.text)
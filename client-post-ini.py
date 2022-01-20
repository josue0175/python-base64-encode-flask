import base64
import requests

with open('test.ini', 'rb') as f:
    ini_b64 = base64.b64encode(f.read())

print(ini_b64)

payload = {'id': '123', 'iniFile': ini_b64}

url = 'http://127.0.0.1:5000/ini_base64'
my_img = {'iniFile': open('test.ini', 'rb')}
#r = requests.post(url, files=my_img)

r = requests.post(url, files=my_img, data=payload)


# convert server response into JSON format.
print(r.json())


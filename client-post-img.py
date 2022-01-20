import base64
import requests

with open('test.jpg', 'rb') as f:
    im_b64 = base64.b64encode(f.read())

payload = {'id': '123', 'type': 'jpg', 'box': [0, 0, 100, 100], 'image': im_b64}

url = 'http://127.0.0.1:5000/im_size'
my_img = {'image': open('test.jpg', 'rb')}
#r = requests.post(url, files=my_img)

r = requests.post(url, files=my_img, data=payload)


# convert server response into JSON format.
print(r.json())


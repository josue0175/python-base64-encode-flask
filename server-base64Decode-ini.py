import base64
import io
from PIL import Image

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/ini_base64", methods=["POST"])
def process_iniFile():
    #file = request.files['iniFile']
    # Read the iniFile via file.stream
    #img = Image.open(file.stream)
    payload = request.form.to_dict(flat=False)

    ini_b64 = payload['iniFile'][0]  # remember that now each key corresponds to list.
    print(ini_b64)
    ini_binary = base64.b64decode(ini_b64)
    print(ini_binary)
    stream_str = io.BytesIO(ini_binary)
    with open("new.ini", "wb") as f:
        f.write(stream_str.read())
    #buf = io.BytesIO(ini_binary)
    #img = Image.open(buf)

   # return jsonify({'msg': 'success', 'size': [img.width, img.height]})
    #return jsonify({'iniFile': [ini_binary]})
    return jsonify({'msg': 'success'})


if __name__ == "__main__":
    app.run(debug=True)

# see https://jdhao.github.io/2020/03/17/base64_opencv_pil_iniFile_conversion/
# for more info on how to convert base64 iniFile to PIL Image object.
#ini_binary = base64.b64decode(ini_b64)
#buf = io.BytesIO(ini_binary)
#img = Image.open(buf)
#file.save('im-received.jpg')



import io
from flask import Flask, request, send_file
from rembg import remove
from PIL import Image

app = Flask(__name__)

@app.route('/remove-background', methods=['POST'])
def remove_background():
    if 'file' not in request.files:
        return 'No file uploaded', 400
    file = request.files['file']
    input_image = Image.open(file)
    output_image = remove(input_image)
    
    img_io = io.BytesIO()
    output_image.save(img_io, 'PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)

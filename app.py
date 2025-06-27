from flask import Flask, render_template, request, redirect, url_for
import os
import cv2
import numpy as np
import torch

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/results'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load AnimeGAN2 model with torch.hub
model = torch.hub.load(
    'bryandlee/animegan2-pytorch:main',
    'generator',
    pretrained='face_paint_512_v2'
).eval()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))

    if file:
        filename = file.filename
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(upload_path)

        # Load image, apply model
        img = cv2.imread(upload_path)[:, :, [2, 1, 0]]  # BGR -> RGB
        img = cv2.resize(img, (512, 512))
        img = img / 127.5 - 1.0
        img = torch.tensor(img).permute(2, 0, 1).unsqueeze(0).float()

        with torch.no_grad():
            out = model(img)[0]
        out = ((out.permute(1, 2, 0).numpy() + 1) * 127.5).clip(0, 255).astype(np.uint8)
        
        output_filename = 'stylized_' + filename
        output_path = os.path.join(RESULT_FOLDER, output_filename)
        cv2.imwrite(output_path, cv2.cvtColor(out, cv2.COLOR_RGB2BGR))

        return render_template(
            'index.html',
            uploaded_image=filename,
            output_image=output_filename
        )

if __name__ == '__main__':
    app.run(debug=True)

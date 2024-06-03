import os
from flask import current_app, render_template, request, send_from_directory, redirect, url_for
from .utils import pdf_to_jpg

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and file.filename.endswith('.pdf'):
            filename = file.filename
            upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(upload_path)
            output_dir = os.path.join(current_app.config['UPLOAD_FOLDER'], 'output')
            pdf_to_jpg(upload_path, output_dir)
            return redirect(url_for('download_file', filename=filename.split('.')[0] + '_1.jpg'))
    return render_template('index.html')

@app.route('/uploads/<filename>')
def download_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)

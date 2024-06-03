from flask import Blueprint, render_template, request, redirect, url_for, current_app, send_from_directory
import os
from .utils import pdf_to_jpg

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            return redirect(request.url)
        
        if file and file.filename.endswith('.pdf'):
            filename = file.filename
            upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(upload_path)
            
            output_dir = os.path.join(current_app.config['UPLOAD_FOLDER'], 'output')
            pdf_to_jpg(upload_path, output_dir)
            
            # Assuming you want to redirect to the first converted image
            return redirect(url_for('routes.download_file', filename=filename.split('.')[0] + '_1.jpg'))
    
    return render_template('index.html')

@bp.route('/uploads/<filename>')
def download_file(filename):
    # Ensure the output directory path is correctly handled
    return send_from_directory(os.path.join(current_app.config['UPLOAD_FOLDER'], 'output'), filename)

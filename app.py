from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Route برای صفحه اصلی
@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=files)

# Route برای آپلود فایل
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        flash('File successfully uploaded')
        return redirect(url_for('index'))

# Route برای دانلود فایل
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Route برای حذف فایل
@app.route('/delete/<filename>')
def delete_file(filename):
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    flash(f'{filename} has been deleted')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from PIL import Image
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

def resize_image(image, new_width=100):
    """
    Resize the image to the specified width while maintaining aspect ratio.
    """
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    """
    Convert the image to grayscale.
    """
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image):
    """
    Map each pixel to an ASCII character based on the range of gray levels.
    """
    ASCII_CHARS = "@%#*+=-:. "
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        # Ensure pixel value is within bounds
        pixel_value = max(0, min(255, pixel_value))
        ascii_index = min(pixel_value // 25, len(ASCII_CHARS) - 1)
        ascii_char = ASCII_CHARS[ascii_index]
        ascii_str += ascii_char
    return ascii_str

def resize_ascii(ascii_art, scale_factor=0.5):
    """
    Scale down the ASCII art by a certain factor.
    """
    lines = ascii_art.split('\n')
    scaled_ascii = ''
    for line in lines:
        scaled_line = ''
        for char in line:
            scaled_line += char * int(scale_factor)
        scaled_ascii += scaled_line + '\n'
    return scaled_ascii


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            now = datetime.now()
            folder_name = now.strftime("%Y-%m-%d_%H-%M-%S")
            folder_path = os.path.join(app.config['UPLOAD_FOLDER'], folder_name)
            os.makedirs(folder_path, exist_ok=True)
            filename = secure_filename(file.filename)
            filepath = os.path.join(folder_path, filename)
            file.save(filepath)
            original_image = Image.open(filepath)
            original_image_path = os.path.join('uploads', folder_name, filename)
            ascii_image = resize_image(grayify(original_image))
            ascii_str = pixels_to_ascii(ascii_image)
            ascii_art = ""
            for i in range(0, len(ascii_str), ascii_image.width):
                ascii_art += ascii_str[i:i+ascii_image.width] + "\n"
            ascii_filename = os.path.splitext(filename)[0] + ".txt"
            ascii_filepath = os.path.join(folder_path, ascii_filename)
            with open(ascii_filepath, 'w') as f:
                f.write(ascii_art)
            flash('Image uploaded successfully')
            return render_template('index.html', original_image=original_image_path, ascii_art=ascii_art)
    return render_template('index.html')

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)

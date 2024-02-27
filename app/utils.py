# Import necessary modules
import os
from flask import current_app

# Function to check if the file extension is allowed
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to save the uploaded image
def save_uploaded_image(file):
    # Create a directory for storing uploaded images if it doesn't exist
    upload_folder = os.path.join(current_app.root_path, 'static/images')
    os.makedirs(upload_folder, exist_ok=True)

    # Save the uploaded image with a unique filename
    filename = os.path.join(upload_folder, file.filename)
    file.save(filename)

    # Return the path to the saved image
    return filename

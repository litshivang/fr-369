# Import necessary modules
from flask import Blueprint, request, jsonify
from app.utils import allowed_file, save_uploaded_image
from app.models.face_recognition_model import recognize_faces

# Create a Blueprint for routes
api_bp = Blueprint('api', __name__)

# Route for uploading an employee image
@api_bp.route('/upload', methods=['POST'])
def upload_image():
    # Check if the POST request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    # If the user does not select a file, the browser may send an empty file without a filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Check if the file extension is allowed
    if file and allowed_file(file.filename):
        # Save the uploaded image
        image_path = save_uploaded_image(file)
        return jsonify({'message': 'Image uploaded successfully', 'image_path': image_path}), 200
    else:
        return jsonify({'error': 'File type not allowed'}), 400

# Route for performing face recognition
@api_bp.route('/recognize', methods=['POST'])
def recognize():
    # Check if the POST request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    # If the user does not select a file, the browser may send an empty file without a filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Check if the file extension is allowed
    if file and allowed_file(file.filename):
        # Perform face recognition
        result = recognize_faces(file)
        return jsonify(result), 200
    else:
        return jsonify({'error': 'File type not allowed'}), 400

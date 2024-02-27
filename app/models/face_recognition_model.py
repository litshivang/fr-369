# Import necessary modules
import os
from deepface import DeepFace

# Function to perform face recognition
def recognize_faces(image):
    # Define the path to the directory containing employee images
    images_dir = 'assets/images'  # Update this path as per your project structure

    # List all files in the directory
    employee_files = os.listdir(images_dir)

    # Load the face recognition model
    model = DeepFace.build_model("Facenet")

    # Loop through each employee image
    for employee_file in employee_files:
        # Load the employee image
        employee_image_path = os.path.join(images_dir, employee_file)
        employee_image = DeepFace.detectFace(employee_image_path, detector_backend='opencv')

        # Perform face recognition
        try:
            if len(employee_image) == 0:
                continue  # Skip if no face is detected in the employee image
            result = DeepFace.verify(image, employee_image[0], model=model, detector_backend='opencv')
            if result["verified"]:
                # Return the employee ID or name associated with the image
                return {'message': 'Face recognized successfully', 'employee_id': employee_file.split('_')[0]}, 200
        except Exception as e:
            return {'error': str(e)}, 500

    # If no match is found, return an error message
    return {'error': 'Face not recognized'}, 400

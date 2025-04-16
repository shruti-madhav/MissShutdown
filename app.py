import cv2
import os
import numpy as np
from flask import Flask
import face_recognition
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("in func")
    return render_template("index.html")


# Compare the new face encoding with the saved encoding
def recognize_user(new_face_encoding):
    # Load the saved encoding
    saved_encoding = np.load("user_face_encoding.npy")
    
    # Compare the new face with the saved encoding
    results = face_recognition.compare_faces([saved_encoding], new_face_encoding)
    
    if results[0]:
        print("User recognized!")
        return True
    else:
        print("User not recognized.")
        return False
    
    
@app.route("/smiled", methods=['POST'])
def smile():
    print("smile")

    # Check if the user face encoding already exists
    encoding_file = "user_face_encoding.npy"
    
    if os.path.exists(encoding_file):
        # Load the saved user face encoding
        user_encoding = np.load(encoding_file)
        print("Using saved user face encoding.")
    else:
        # If no saved encoding, capture a new image and save the encoding
        name = request.form.get("name")
        cap = cv2.VideoCapture(0)
        cv2.waitKey(1000)

        # Capture a frame
        ret, frame = cap.read()
        cap.release()

        # Detect face locations and encodings
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        if face_encodings:
            # Save the first face encoding (assuming only one user)
            user_encoding = face_encodings[0]
            
            # Save encoding to a file using numpy
            np.save(encoding_file, user_encoding)
            print("User face encoding saved.")
        else:
            print("No face detected.")
            return "No face detected. Please try again."

    # Now you can use `user_encoding` for recognition in future requests
    # For future requests, compare the captured face encoding to the saved encoding
    # For example:
    # new_face_encoding = get_face_encoding_from_current_frame()
    # if compare_faces(new_face_encoding, user_encoding):
    #     print("User recognized!")
    return "Smile detected!"


if __name__ == "__main__":
    app.run(debug=True)




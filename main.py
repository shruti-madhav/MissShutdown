import numpy as np
import cv2
import mediapipe as mp
import os
import platform


cap = cv2.VideoCapture(0)


mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

def is_finger_up(lmList, tip_id, pip_id):
    return lmList[tip_id].y < lmList[pip_id].y

def shutdown_computer():
    os_name = platform.system()
    print("Shutting down...")
    if os_name == "Windows":
        os.system("shutdown /s /t 1")
    elif os_name == "Linux" or os_name == "Darwin":
        os.system("shutdown now")
    else:
        print("Unsupported OS for shutdown")

peace_triggered = False  # To avoid multiple shutdown calls

while True:
    ret, img = cap.read()
    if not ret:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            h, w, c = img.shape
            lmList = []

            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append(lm)
                if id == 0:  # Use wrist for palm bounding box center
                    palm_x, palm_y = cx, cy
                    palm_w = int(0.1 * w)
                    palm_h = int(0.15 * h)
                    cv2.rectangle(img, (palm_x - palm_w//2, palm_y - palm_h//2),
                                  (palm_x + palm_w//2, palm_y + palm_h//2), (0, 255, 0), 2)

            if len(lmList) >= 21:
                index_up = is_finger_up(lmList, 8, 6)
                middle_up = is_finger_up(lmList, 12, 10)
                ring_up = is_finger_up(lmList, 16, 14)
                pinky_up = is_finger_up(lmList, 20, 18)

                if middle_up:
                    cv2.putText(img, "Peace - Shutting down...", (50, 100),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    if not peace_triggered:
                        peace_triggered = True
                        cap.release()
                        cv2.destroyAllWindows()
                        # shutdown_computer()

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow('Peace Sign Shutdown', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()























"""
import os
import cv2
import face_recognition
import numpy as np
from flask import request

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
    # For example: Talk to the hand Miss Shutdown SassyShutdown OffendedBot F.U. GestureX

    # new_face_encoding = get_face_encoding_from_current_frame()
    # if compare_faces(new_face_encoding, user_encoding):
    #     print("User recognized!")
    return "Smile detected!"


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


# result = recognize_user(user_encoding)
# if result:
#     return f"Welcome back, {name}!"
# else:
#     return f"Hey {name}"

"""
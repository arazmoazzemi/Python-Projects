import cv2
from deepface import DeepFace

class VideoProcessor:
    def __init__(self):
        # Load Haar Cascade for face detection
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def process_frame(self, frame):
        # Detect faces in the frame
        faces = self.face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]

            # Check face size threshold
            min_face_size = (50, 50)
            if w < min_face_size[0] or h < min_face_size[1]:
                continue

            # Analyze facial emotion using DeepFace
            try:
                results = DeepFace.analyze(face, actions=['emotion'], enforce_detection=False)
                # Access emotion directly from the list
                emotion = results[0]['dominant_emotion'] if results else "Not Detected"
            except Exception as e:
                print(f"Error during emotion analysis: {e}")
                emotion = "Not Detected"

            # Display the emotion result
            cv2.putText(frame, f'Emotion: {emotion}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        return frame

# Open a connection to the webcam (camera index 0 by default)
cap = cv2.VideoCapture(0)

# Create a VideoProcessor instance
video_processor = VideoProcessor()

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Process the frame using the VideoProcessor
    processed_frame = video_processor.process_frame(frame)

    # Display the processed frame
    cv2.imshow('Real-Time Facial Expression Recognition', processed_frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

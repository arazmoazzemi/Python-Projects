
from flask import Flask, render_template
from flask_socketio import SocketIO
import cv2
import numpy as np
import base64
from deepface import DeepFace

app = Flask(__name__)
socketio = SocketIO(app)

class VideoProcessor:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def process_frame(self, frame):
        faces = self.face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            min_face_size = (50, 50)
            if w < min_face_size[0] or h < min_face_size[1]:
                continue
            try:
                results = DeepFace.analyze(face, actions=['emotion'], enforce_detection=False)
                emotion = results[0]['dominant_emotion'] if results else "Not Detected"
            except Exception as e:
                print(f"Error during emotion analysis: {e}")
                emotion = "Not Detected"
            cv2.putText(frame, f'Emotion: {emotion}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return frame

video_processor = VideoProcessor()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('frame')
def handle_frame(data):
    img = base64.b64decode(data)
    npimg = np.frombuffer(img, dtype=np.uint8)
    frame = cv2.imdecode(npimg, 1)
    processed_frame = video_processor.process_frame(frame)
    _, buffer = cv2.imencode('.jpg', processed_frame)
    response = base64.b64encode(buffer).decode('utf-8')
    socketio.emit('response_frame', response)

if __name__ == '__main__':
    socketio.run(app)

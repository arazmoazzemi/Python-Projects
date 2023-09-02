# YOLOV8

Start 

clone yolov8 form github

```
git clone https://github.com/ultralytics/ultralytics.git
cd ultralytics
pip install -r requirements.txt

```













----------------------------------------------------------
# Build Your Own Face Recognition Tool With Python

https://realpython.com/face-recognition-with-python/




-------------------------------------------------------





from google.colab import drive
drive.mount('/content/gdrive')



!python -m pip install --upgrade pip
!pip install tensorflow
!pip install tensorboard


!pip install torch



import torch
from IPython.display import Image



%ls
%cd MyDrive/
!git clone https://github.com/ultralytics/yolov5


%cd yolo5
!pip install -r requirements.txt

!python detect.py --weights yolov5m.pt --source /content/gdrive/MyDrive/tehran.jpg

!python detect.py --weights yolov5m.pt --conf-thres 0.7 --source /content/gdrive/MyDrive/tehran.jpg


python detect.py --weights yolov5m.pt --conf-thres 0.7 --source C:\Users\DevOps\PycharmProjects\pythonProject\tehran.jpg
python detect.py --weights yolov5m.pt  --source C:\Users\DevOps\PycharmProjects\pythonProject\test.mp4
python detect.py --weights yolov5m.pt  --source C:\Users\DevOps\PycharmProjects\pythonProject\tehran.jpg --class 0 3



python detect.py --weights yolov5m.pt  --source rtsp://admin:mrns2468@192.168.86.211:554/Streaming/Channels/1/






------------picture--------------------------

import torch
from IPython.display import Image

import torch
import cv2

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5m')

# Load an image
image_path = 'C:\\Users\\DevOps\\PycharmProjects\\pythonProject\\tehran.jpg'
img = cv2.imread(image_path)

# Perform object detection
results = model(img)

# Display the results
results.show()

# Save the results
results.save()

# Access the bounding box coordinates and class labels
boxes = results.xyxy[0].numpy()  # Bounding box coordinates
labels = results.names[0]  # Class labels

# Process the bounding boxes and class labels as needed
for box in boxes:
    x1, y1, x2, y2, confidence, class_id = box
    label = labels[int(class_id)]
    # Process the bounding box and label
    print(f'Bounding box: {box}, Label: {label}')







-------------webcam------------------------------------

import cv2
import torch
from PIL import Image

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Set device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

# Load webcam
cap = cv2.VideoCapture(0)

while True:
    # Read frame from webcam
    ret, frame = cap.read()

    # Convert frame to PIL Image
    frame = Image.fromarray(frame[:, :, ::-1])

    # Perform object detection
    results = model(frame)

    # Display results
    results.show()

    # Press 'q' to exit
    if cv2.waitKey(1) == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()










--------------------------------------train---------------------------
https://www.cvat.ai/#

https://makesense.ai



python train.py --img 640 --batch 16 --epochs 3 --data custom_data.yaml --weights yolov5s.pt --cache


----------custom_data.yaml--------------------

# YOLOv5 🚀 by Ultralytics, AGPL-3.0 license
# COCO128 dataset https://www.kaggle.com/ultralytics/coco128 (first 128 images from COCO train2017) by Ultralytics
# Example usage: python train.py --data coco128.yaml
# parent
# ├── yolov5
# └── datasets
#     └── coco128  ← downloads here (7 MB)


# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
train : ../train_data/images/train
val : ../train_data/images/val
# Classes
names:
  0: Araz Moazzemi
  

# Download script/URL (optional)
download: https://ultralytics.com/assets/coco128.zip


----------------------------------------------------------

runs\train\exp4\weights\last.pt

python detect.py --weights runs\train\exp4\weights\last.pt  --img 640 --source 0


python detect.py --weights runs\train\exp7\weights\last.pt  --img 640 --source C:\Users\IT\PycharmProjects\pythonProject\yolov5\train_data\images
 



---------------------------------------------------------------------------------------------
----------------------------------------yolov8-----------------------------------------------
---------------------------------------------------------------------------------------------

git clone https://github.com/ultralytics/ultralytics.git

cd ultralytics

pip install -r requirements.txt


yolo task=detect mode=predict model=yolov8n.pt conf=0.25 source="input/dogs_n_cars.jpg" save=True

{task=detect / task=segment / task=classification}

{model=yolo8n / model=yolo8s / model=yolo8m / model=yolo8l / model=yolo8x}
































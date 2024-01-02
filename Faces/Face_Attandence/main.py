import pickle
import cv2, os
import numpy as np
import face_recognition
import cvzone


cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('Resources/background.png')

# Import the model images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

# print(len(imgModeList))


# Load the encoding file
print("Loadning Encode File ...")
file = open('EncodeFile.p', 'rb')
encodelistKnownWithIds = pickle.load(file)
file.close()
encodelistKnown, studentIds = encodelistKnownWithIds
# print(studentIds)
print("Encode File Loaded ...")


while True:
    success, img = cap.read(cv2.CAP_DSHOW)

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25, 0)
    imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)


    imgBackground[162:162+480, 55:55+640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[1]


    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodelistKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodelistKnown, encodeFace)

        # print("matches", matches)
        # print("faceDis", faceDis)

        matcheIndex = np.argmin(faceDis)
        print("Match Index", matcheIndex)

        if matches[matcheIndex]:
            # print("Known Face Detected")
            # print(studentIds[matcheIndex])
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
            imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)


    cv2.imshow('Webcam', img)
    cv2.imshow('Face Attendance', imgBackground)
    cv2.waitKey(1)

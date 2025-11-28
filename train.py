import cv2
import os
import numpy as np
import json

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []
label_map = {}
current_label = 0

for pessoa in os.listdir("faces"):
    label_map[current_label] = pessoa
    for img_path in os.listdir(f"faces/{pessoa}"):
        img = cv2.imread(f"faces/{pessoa}/{img_path}", 0)
        faces.append(img)
        labels.append(current_label)
    current_label += 1

recognizer.train(faces, np.array(labels))
recognizer.save("modelo_faces.yml")

with open("labels.json", "w") as f:
    json.dump(label_map, f)


print("Treinamento concluído!")
print(label_map)

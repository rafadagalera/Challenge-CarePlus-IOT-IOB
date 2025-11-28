import cv2
import json

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("modelo_faces.yml")


with open("labels.json", "r") as f:
    label_map = json.load(f)


cap = cv2.VideoCapture(0)

while True:
    ok, frame = cap.read()
    if not ok:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        rosto = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(rosto)

        # =========================
        # METHOD 1 — convert to %
        # =========================
        percent = max(0, 100 - confidence)

        nome = label_map.get(str(label), "DESCONHECIDO")

        text = f"{nome} ({percent:.1f}%)"
        cv2.rectangle(frame, (x,y-25), (x+w, y), (0,255,0), -1)  # filled rectangle
        cv2.putText(frame, text, (x+5, y-5),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 2)
 

    cv2.imshow("Reconhecimento Facial", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

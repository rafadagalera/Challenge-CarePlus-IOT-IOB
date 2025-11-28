import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("modelo_faces.yml")

label_map = {
    0: "Pessoa1",
    1: "Pessoa2"
}

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

        nome = label_map.get(label, "DESCONHECIDO")

        cv2.putText(frame, f"{nome}  ({percent:.1f}%)",
                    (x, y-10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0,255,0),2)

        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Reconhecimento Facial", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

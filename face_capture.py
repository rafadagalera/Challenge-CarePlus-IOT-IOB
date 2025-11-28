import cv2
import os

# Cria pasta pra salvar rostos
nome_pessoa = input("Nome da pessoa: ")
path = f"faces/{nome_pessoa}"
os.makedirs(path, exist_ok=True)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

contador = 0

while True:
    ok, frame = cap.read()
    if not ok:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        rosto = gray[y:y+h, x:x+w]
        cv2.imwrite(f"{path}/{contador}.jpg", rosto)
        contador += 1

        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Captura de rostos", frame)
    if cv2.waitKey(1) == ord('q') or contador >= 200:
        break

cap.release()
cv2.destroyAllWindows()

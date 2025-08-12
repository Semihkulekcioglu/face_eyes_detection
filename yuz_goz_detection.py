import numpy as np
import cv2

# Haar Cascade dosyalarının yüklenmesi
face_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
eye_cascade_path = cv2.data.haarcascades + 'haarcascade_eye.xml'

#face ve eyes için
face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

#webcam açılış vs

#cap = cv2.VideoCapture("video1.mp4")
cap = cv2.VideoCapture(0)

while True:
    _,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 4)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        #göz için 2 den fazla değer okunmaması için i=0 ile düzenlemeler
        eyes = eye_cascade.detectMultiScale(roi_gray)
        i=0
        for(ex, ey, ew, eh) in eyes:
            i+=1
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,0,255),2)
            if(i==2):
                break
            
    cv2.imshow("baslik", img)
    k = cv2.waitKey(30) & 0xff      #ESC tuşuyla kamera kapatılır.
    
    if k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
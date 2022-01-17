import cv2
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_glass = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml") 
   
while True:
    ret, frame = cap.read()

    faces = face_cascade.detectMultiScale(frame,2,5)       

    for x,y,w,h in faces:
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(frame,'Anant',(x+w,y+h),font,1,(250,250,250),1,cv2.LINE_AA)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),2)       
        roi_color = frame[y:y+h, x:x+w]
        eye_g = eye_glass.detectMultiScale(roi_color)
        for (ex,ey,ew,eh) in eye_g:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)


    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

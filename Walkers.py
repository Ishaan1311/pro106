import cv2
img = cv2.imread("walking.avi")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
body_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces = body_classifier.detectMultiScale(gray,1.1,5)
print(faces)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_color = img[y:y+h,x:x+w]
    cv2.imwrite("face.jpg",roi_color)
   
    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
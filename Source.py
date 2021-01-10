import cv2

detector=cv2.CascadeClassifier('C:/Users/Tanmay/Desktop/eye.xml')

cap = cv2.VideoCapture(0)

while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eye = detector.detectMultiScale(gray, 1.5, 5)
    for (x,y,w,h) in eye:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('frame',img)
    cv2.imwrite('ashu.jpg',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
x=5
for i in range(0,1):
    print((x))

cap.release()
cv2.destroyAllWindows()
exit()

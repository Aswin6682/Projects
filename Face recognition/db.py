import numpy as np
import cv2
import sqlite3
detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
rec=cv2.createLBPHFaceRecognizer();
rec.load("recognizer\\trainningdata.yml")
id=0
attendance=0
def insert(Id,attendance):
    conn=sqlite3.connect("facebase.db")
    cmd="SELECT * FROM People WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    isrecordexist=0
    for row in cursor:
        isrecordexist=1
    if(isrecordexist==1):
        cmd="UPDATE People SET attendance="+str(attendance)+" WHERE ID="+str(Id)
    conn.execute(cmd)
    conn.commit()
    conn.close
    
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    if(len(faces)!=0):
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            id,conf=rec.predict(gray[y:y+h,x:x+w])
            if(id==1):
                id="varshu"
                Id=1
                attendance=1
                insert(Id,attendance)

            if(id==2):
                id="naveen"
                Id=2
                attendance=1
                insert(Id,attendance)

      
            cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255);    

    cv2.imshow('face',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print at
print at1    
cap.release()
cv2.destroyAllWindows()

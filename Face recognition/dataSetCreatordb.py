import cv2
cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
import sqlite3
def insert(Id,Name):
    conn=sqlite3.connect("facebase.db")
    cmd="SELECT * FROM Project where ID="+str(Id)
    cursor=conn.execute(cmd)
    exist=0
    for row in cursor:
        exist=1
    if(exist==1):
        cmd="UPDATE Project SET Name='"+str(Name)+"' WHERE ID="+str(Id)
    else:
        cmd="INSERT INTO Project(ID,Name) Values("+str(Id)+",'"+str(Name)+"')"
    conn.execute(cmd)
    conn.commit()
    conn.close()
Id=raw_input('enter your id')
Name=raw_input('enter your name')
insert(Id,Name)
sampleNum=0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        #incrementing sample number 
        sampleNum=sampleNum+1
        #saving the captured face in the dataset folder
        cv2.imwrite("dataSet/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('frame',img)
    #wait for 100 miliseconds 
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    # break if the sample number is morethan 20
    elif sampleNum>20:
        break
cam.release()
cv2.destroyAllWindows()

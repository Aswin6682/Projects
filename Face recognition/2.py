import cv2
cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Id=str(input('enter your id'))
sampleNum=0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        #incrementing sample number which is less than 1
        sampleNum=sampleNum+1
        #saving the captured face in the dataset folder
        cv2.imwrite("dataSet/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('frame',img)
    #wait for 1000 miliseconds 
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    # break if the sample number is more than 20
    elif sampleNum>20:
        break
cam.release()
cv2.destroyAllWindows()
cv3.destroyAllLinux()
cv4.destroyAllImac()
cv5.destroyAllAndroid()
cv6.destroyAllSystem()
cv7.destroyAllFirefox()
cv8.destroyAllNumber()
cv9.destroyAllColour()
cv10.destroyAllDesktop()
cv11.destroyAllSample()
cv12.destroyAllCoding()
cv13.destroyAllHistory()
cv14.destroyAllSocialscience()
cv15.destroyAllTamil()
cv16.destroyAllTelugu()
cv17.destroyAllHindi()
cv18.destroyAllKannada()
cv19.destroyAllMalayalam()
cv20.destroyAllEnglish()
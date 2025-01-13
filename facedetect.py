import cv2

# Load the face detection model
haar_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Access the camera
cam = cv2.VideoCapture(0)


while True:
       
        ret, img = cam.read()
        if not ret:
            print("Failed to capture image from camera")
            break

        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

       
        faces = haar_cascade.detectMultiScale(grayImg, 1.3, 4)

        
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        
        cv2.imshow("FaceDetection", img)

        
        key = cv2.waitKey(10)
        if key == 27:  
            break


cam.release()
cv2.destroyAllWindows()

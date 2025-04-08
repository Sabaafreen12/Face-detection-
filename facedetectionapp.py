import cv2
def captureImage(video_data):
    ImgName="opencamera1.png"
    cv2.imwrite(ImgName,video_data)
    print(f"your image is saved as {ImgName}")
camera=cv2.VideoCapture(0)
face_Capture=cv2.CascadeClassifier(".venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
while True:
    success,video_data=camera.read()
    color=cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
    face=face_Capture.detectMultiScale(color,1.1,5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
    for (x,y,w,h) in face:
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)
    if not success:
        print("failed to capture video")
    else:
        cv2.imshow('my cam',video_data)
    keyEvent=cv2.waitKey(1)
    if keyEvent==ord('c'):
        captureImage(video_data)

    if cv2.waitKey(1)==ord('q'):

        break
        
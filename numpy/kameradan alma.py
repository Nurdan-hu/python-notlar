import cv2
xxx= cv2.VideoCapture(0)
while True:
    ret , kare = xxx.read()
    cv2.imshow('Pencere', kare)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break

xxx.release()
cv2.destroyAllWindows()
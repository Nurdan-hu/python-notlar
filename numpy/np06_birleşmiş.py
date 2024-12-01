import cv2
import numpy as np

r1 = np.full((50,150,3),[255,0,0], dtype= np.uint8)
r2 = np.full((50,150,3) , [255,0,255] , dtype= np.uint8)

print(r1)
cv2.imshow("Oluşan resim" , r1)
cv2.imshow("Oluşan resim2" , r2)

birleşik = cv2.hconcat([r1,r2])
cv2.imshow("Oluşan resim3" , birleşik)

cevrilmis = cv2.rotate(birleşik,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Oluşan resim4" , cevrilmis)

cv2.waitKey(0)
cv2.destroyAllWindows()
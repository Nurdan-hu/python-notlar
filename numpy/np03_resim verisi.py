# boş resim oluşturma
import cv2
import numpy as np

# aşağıdaki [255, 255, 255] rakamlarını oynayarak ne olduğuna bakın
r1= np.full((100, 500, 3), [255, 100, 0], dtype=np.uint8) #100 satır, 500 sütun , 3'lü diziler

print(r1)
cv2.imshow("Olusan resim", r1)

cv2.waitKey(0)
 
cv2.destroyAllWindows()

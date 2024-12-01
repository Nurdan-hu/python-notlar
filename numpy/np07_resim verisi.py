import numpy as np
from numpy import random
import cv2

x1 = random.randint(100)

r5 = np.full((50,170,3) , [random.randint(255) ,0, random.randint(255)] , dtype= np.uint8)
cv2.imshow("Oluşan resim5", r5)

cv2.waitKey(0)
cv2.destroyAllWindows()
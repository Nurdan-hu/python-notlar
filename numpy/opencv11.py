#  Ör-2: Resim açma
import cv2
img = cv2.imread('images/square.jpg')
cv2.imshow('Deneme',img)
cv2.waitKey(3000) # 3 saniye bekle
cv2.destroyAllWindows() # pencereleri kapa


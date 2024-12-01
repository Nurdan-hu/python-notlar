import numpy as np
arr1 = np.zeros((3,4))
print(arr1)

arr1 = np.ones((3,4))
print(arr1)

liste = []
liste_ = []
for a in range(30):
    for b in range(40):
        liste_.append(b)
    liste.append(liste_)
print (liste)
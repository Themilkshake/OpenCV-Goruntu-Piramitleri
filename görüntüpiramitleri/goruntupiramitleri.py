import numpy as np
import cv2

resim1=cv2.imread("kus.jpg")


"""
cv2.pyrUp(resim1):
Üstteki resmin aynısının iki katını yeni resim olarak tanımlıyor.

cv2.pyrDown(resim1):
Üstteki resmin aynısının yarı katını yeni resim olarak tanımlıyor.

pyr: piramid.
"""

resim1_2k=cv2.pyrUp(resim1)
resim1_05k=cv2.pyrDown(resim1)

cv2.imshow("resim1_05k",resim1_05k)
cv2.imshow("resim1_2k",resim1_2k)

print(resim1_2k.shape)
print(resim1_05k.shape)

""" 
Resmi istediğimiz bir biçimde boyutlandırıyor.
resim3=cv2.resize(yeniden boyutlandırılacak resim,(genişlik,yükseklik))
"""


resim3=cv2.resize(resim1,(600,500))
cv2.imshow("resize",resim3)



cv2.waitKey(0)
cv2.destroyAllWindows()


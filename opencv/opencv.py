import cv2
img = cv2.imread("images (1).jpg",0) # resim dosyasını okur,0 gri tonlamalı okunacağını belirtir
print(img)
"""cv2.IMREAD_UNCHANGED  = -1   # alfa kanalı dahil, orijinal haliyle
cv2.IMREAD_GRAYSCALE  =  0   # gri tonlama
cv2.IMREAD_COLOR      =  1   # renkli (BGR), varsayılan"""
cv2.namedWindow("resim",cv2.WINDOW_NORMAL) # pencere boyutunu ayarlamak için
cv2.imshow("resim",img) # resmi ekranda gösterir
cv2.imwrite("resim_kopya.jpg",img) # resmi kopyalar ve kaydeder
cv2.waitKey(0) # herhangi bir tuşa basılmasını bekler
cv2.destroyAllWindows() # tüm pencereleri kapatır
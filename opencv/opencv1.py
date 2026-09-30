import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), np.uint8) +255
"""
cv2.line(canvas, (100,100),(300,300),(0,0,255), 5) #çizgi oluşturma bu şekilde yapılır. cv2.line(canvas,başlangıç noktası, bitiş noktası, renk, kalınlık)
cv2.line(canvas,(300,350),(400,500),(255,0,0),8)
"""

cv2.rectangle(canvas,(100,100),(300,300),(0,0,255),5) # dikdörtgen oluşturma cv2.rectangle(canvas,başlangıç noktası, bitiş noktası, renk, kalınlık)

cv2.circle(canvas,(100,100),60,(255,0,0),4) # daire oluşturma cv2.circle(canvas,merkez noktası,yarıçap,renk,kalınlık)

u1 = (300,500)
u2 = (300,400)
u3 = (500,300)

cv2.line(canvas,u1,u2,(0,255,0),5) # üçgen oluşturma cv2.line(canvas,başlangıç noktası, bitiş noktası, renk, kalınlık)
cv2.line(canvas,u2,u3,(0,255,0),5)  
cv2.line(canvas,u3,u1,(0,255,0),5)

f1 = cv2.FONT_ITALIC
f2 = cv2.FONT_HERSHEY_COMPLEX
f3 = cv2.CAP_AVFOUNDATION

cv2.putText(canvas,"Merhaba",(100,400),f1,1,(0,0,255),2) # yazı ekleme cv2.putText(canvas,yazı,(başlangıç noktası),font tipi,font boyutu,renk,kalınlık) 

cv2.imshow("pencere", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

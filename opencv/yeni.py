
import cv2

# Kurulan OpenCV versiyonunu ekrana yazdırır
#print("OpenCV Versiyonu:", cv2.__version__)

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)  # 0, varsayılan kamera cihazını temsil eder
dosyaadi="C:\deneme.mp4"  # Kaydedilecek dosya adı ve yolu
codec=cv2.VideoWriter_fourcc(*"mp4v")  # Video codec'i belirler
framerate=30  # Kare hızı (frame per second)
resolution=(640,480)  # Video çözünürlüğü (genişlik, yükseklik)
out=cv2.VideoWriter(dosyaadi,codec,framerate,resolution)  # VideoWriter nesnesi oluşturur

while True:
    ret, frame=cap.read()
    frame=cv2.flip(frame,1)  # Görüntüyü yatay olarak çevir
    cv2.imshow("Kamera", frame)
    out.write(frame)  # Görüntüyü video dosyasına yaz
    if cv2.waitKey(1) & 0xFF==ord("b"):  # 'b' tuşuna basıldığında döngüden çık
        break
   
    cv2.waitKey(30)  # 1 milisaniye bekler

cap.release()  # Kamera cihazını serbest bırakır
cv2.destroyAllWindows()  # Tüm OpenCV pencerelerini kapatır    
import cv2
import numpy as np

# Kamerayı başlat (0 = varsayılan webcam)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # BGR'den HSV renk uzayına çevir
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Mavi rengin HSV aralığı (alt ve üst sınır)
    alt_mavi = np.array([100, 150, 50])
    ust_mavi = np.array([140, 255, 255])

    # Sadece bu aralıktaki pikselleri beyaz, geri kalanı siyah yapan maske
    mask = cv2.inRange(hsv, alt_mavi, ust_mavi)

    # Maskedeki nesnelerin konturlarını (dış hatlarını) bul
    konturlar, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for kontur in konturlar:
        alan = cv2.contourArea(kontur)
        if alan > 500:  # çok küçük gürültüleri (noise) yok say
            x, y, w, h = cv2.boundingRect(kontur)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, "Mavi Tespit Edildi", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # Sonuçları göster
    cv2.imshow("Orijinal Goruntu", frame)
    cv2.imshow("Maske", mask)

    # 'q' tuşuna basınca çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
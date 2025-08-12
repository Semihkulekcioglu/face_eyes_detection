# Yüz ve Göz Tespiti Projesi

OpenCV ve Haar Cascade sınıflandırıcıları kullanarak gerçek zamanlı yüz ve göz tespiti yapan uygulama.

## Özellikler

- Webcam kullanarak gerçek zamanlı yüz tespiti
- Tespit edilen yüzlerde göz tespiti
- Video dosyası girişi desteği
- Tespit edilen yüzler etrafında yeşil dikdörtgenler
- Tespit edilen gözler etrafında kırmızı dikdörtgenler

## Gereksinimler

- Python 3.7+
- OpenCV
- NumPy

## Kurulum

1. Depoyu klonlayın:
```bash
git clone https://github.com/Semihkulekcioglu/face_eyes_detection.git
cd face_eyes_detection
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

## Kullanım

### Webcam Modu
```bash
python face_eyes_detection.py
```

### Video Dosyası Modu
Video dosyaları ile kullanmak için kodda bu satırı yorum işaretini kaldırın ve düzenleyin:
```python
cap = cv2.VideoCapture("video1.mp4")
```

## Kontroller

- Uygulamadan çıkmak için `ESC` tuşuna basın

## Proje Yapısı

- `face_eyes_detection.py` - Ana uygulama dosyası
- `requirements.txt` - Python bağımlılıkları
- `video1.mp4`, `video2.mp4`, `video3.mp4` - Test için örnek video dosyaları

## Nasıl Çalışır

Uygulama yüz ve göz tespiti için Haar Cascade sınıflandırıcılarını kullanır:
1. Webcam veya video dosyasından video yakalar
2. İşleme için kareleri gri tonlamaya dönüştürür
3. `haarcascade_frontalface_default.xml` kullanarak yüzleri tespit eder
4. Her tespit edilen yüz için `haarcascade_eye.xml` kullanarak gözleri tespit eder
5. Tespit edilen yüz ve gözler etrafında sınırlayıcı kutular çizer
6. Yüz başına maksimum 2 göz tespiti ile sınırlar

## Screenshot
<img width="640" height="640" alt="Result" src="https://github.com/user-attachments/assets/902f90d6-0377-44a6-adae-a48f7c4f4bd8" />

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için LICENSE dosyasına bakın.

import cv2                                          # openCV  kütüphanesini projeye dahil etme
cap = cv2.imread('arabalar.jpg')                       #imread = image+read / araç sayılacak görseli tanımlama(bu .py dosyası ile aynı konumda olmalı)
car_cascade = cv2.CascadeClassifier('cascade.xml')  #bulunacak nesnenin tanımlı olduğu xml dosyası. ister internetten indirin. ister Cascade Trainer programi ile kendiniz oluşturun 
gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)        #görsel üzerinde işlem yapabilmek için bunu gri tonlamalı hale dönüştümemiz lazım
cars = car_cascade.detectMultiScale(gray, 1.1, 3)   #görsel içinde aranan nesnenin bulunduğu kısım.(griTonlamalıGöresel, KontrastOranı, IterasyonSayısı) /bu değerler sabit değil en iyi sonuç için deneyerek bulun
aracSayisi = 0                                      #görseldeki araç sayısını tutacak değişken
for (x,y,w,h) in cars:                              #cars dediği araçlar tespit edildiğinde bize bir liste döndürür. listenin elemanlarında x=karenin sol üst noktasının soldan uzaklığı, y=sağdan üzeklığı, w=karenin genişliği,h= karenin boyu
    aracSayisi+=1                                   #her for döngüsünün iterasyonu tespit edilen bir araç var demek. o yüzden sayacı 1 artırdık.
    cv2.rectangle(cap,(x,y),(x+w,y+h),(0,255,0),1)  #karenin koordinatlarını renk tonunu ve çizgi kalınlığını belirterek yeşil kutucuk çizdik
    print (x,y,w,h)                                 #ekrana kutuların konumlarını yazdırdık  
print("Toplam Araç Sayısı = "+str(aracSayisi))      #toplam araç sayısını ekrana yazdırdık
cv2.imshow('image',cap)                             #üzerine kareler çizdiğimiz görseli imshow=image+show komutu ile ekranda gösterdik    
cv2.waitKey(0)                                      #kullanıcı herhangi bir tuşa basana kadar bekledik.
cv2.destroyAllWindows()                             #tuşa basıldığında bütün pencereleri kapattık 

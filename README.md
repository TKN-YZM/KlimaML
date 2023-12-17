# Makine Öğrenmesi ile IoT Sistemi Oluşturma

Bu proje, sesli komutlarla klima kontrolünü sağlayan ve arka planda sıcaklık ve nem değerlerini takip eden bir IoT sistemi oluşturmayı amaçlar. Makine öğrenmesi algoritmaları, bu değerleri analiz ederek klima açma/kapama kararlarını otomatik olarak verir.

## Teknolojiler ve Araçlar
- Python / Sklearn / Makine Öğrenmesi Algoritamları
- Arduino / DHT11 Nem Ve Sıcaklık Sensörü
- Sklearn / Linear Model / LogisticRegression
- Sqlite 3 
- Ses Tanıma Teknolojileri / Speech_recognition

## Projenin çalışma mantığı
 Sesli komut ile kişisel asistana "klima aç" komutu gönderildiği zaman arka planda veri tabanına Arduino ve DHT11 nem ve sıcaklık sensörü ile veriler kaydedilir ve ardından makine öğrnemesi algoritaması (Logistic Reg) ile bu veriler eğitilir ve tahminde bulunması sağlanır. Ardından asistanı her çağırdımız zaman makine tahmin ile otomatik klima işlemleri gerçekleştirilir.


<div align="center">
  <img  src="https://github.com/TKN-YZM/KlimaML/blob/master/Z1.jpg" alt="Proje Çizim">
  <img  src="https://github.com/TKN-YZM/KlimaML/blob/master/Z2.jpg" alt="Proje Kod">
</div>

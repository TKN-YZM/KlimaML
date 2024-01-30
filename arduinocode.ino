#include <DHT.h>

#define DHTPIN 8     // DHT11 sensörünün sinyal pini
#define DHTTYPE DHT11  // Kullanılan DHT tipi
int ledPin=  7; // LED pinini 13 olarak tanımla
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT); // LED pinini çıkış olarak ayarla
  dht.begin();
}

void loop() {
  delay(2000);  // 2 saniye bekle
  float humidity = dht.readHumidity();    // Nem değerini oku
  float temperature = dht.readTemperature(); // Sıcaklık değerini oku (Celsius cinsinden)
  Serial.print("H:");
  Serial.print(humidity);
  Serial.print("T:");
  Serial.println(temperature);


  char receivedChar = Serial.read(); // Gelen karakteri oku
  if (receivedChar == '1') { // Eğer '1' karakteri alındıysa
    digitalWrite(ledPin, HIGH); // LED'i yak
    Serial.println("LED açık"); // Durumu seri monitöre yaz
  } else if (receivedChar == '0') { // Eğer '0' karakteri alındıysa
    digitalWrite(ledPin, LOW); // LED'i söndür
    Serial.println("LED kapalı"); // Durumu seri monitöre yaz
  }

  
}

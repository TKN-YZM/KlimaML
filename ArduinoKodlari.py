import MakineAlgort
import serial
import time

ML=MakineAlgort.MakineAlgorit()

class RobotikIslem():

    def __init__(self):
        self.port = 'COM4'
        self.baud_rate=9600
    def sensorDeger(self):

        # Arduino'ya bağlan
        ser = serial.Serial('COM4', 9600)  # Arduino'nun bağlı olduğu seri portu belirtin

        # Arduino'dan veriyi oku
        arduino_data = ser.readline().decode('latin-1').rstrip()

        nem = arduino_data.split("H:")[1].split("T:")[0]
        sicaklik = arduino_data.split("H:")[1].split("T:")[1]
        # Gelen veriyi ekrana yazdır
        print("Nem: ", nem, "Sicaklik: ", sicaklik)

        return[sicaklik,nem]
    def klimaIslemi(self,durum):

        arduino_port = "COM4"  # Arduino'nun bağlı olduğu port (Windows'ta "COMx" olabilir)
        baud_rate = 9600  # Arduino ile aynı baud hızı

        arduino = serial.Serial(arduino_port, baud_rate)
        time.sleep(2)  # Arduino'nun hazır olması için biraz bekle

        arduino.write(str(durum).encode())  # Komutu Arduino'ya gönder

    def otomatikKlima(self):
        data=self.sensorDeger()
        print("Sıcaklık: ",data)
        tahmin=ML.TahminAlgorit(data[0], data[1])
        print("Makine Tahmini:",tahmin)
        if(tahmin==True):
            self.klimaIslemi(1)
            print("Klima oto açıldı")
            return 1


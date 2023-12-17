from pyfirmata import Arduino, util #pip install pyfirmata
import Adafruit_DHT                 #pip install adafruit-circuitpython-dht
import MakineAlgort 


class RobotikIslem():
    
    def __init__(self):
        
        self.port = 'COM4'  #İletişim kurulacağı port
        self.board = Arduino(port)
        
    def sensorDeger(self):
        dht_pin = 2 
        dht_sensor = Adafruit_DHT.DHT11
        nem_deger, sicaklik_deger = Adafruit_DHT.read_retry(dht_sensor, dht_pin)  
        return [sicaklik_deger,nem_deger]

    def klimaIslemi(self,durum):
        self.board.get_pin("d:7:o") #klima (röle) bağlı pin
        if(durum):
             board.digital[7].write(1) #röle aktif edilir
             board.exit()
        else:
            board.digital[pin_numarasi].write(0) #röle kapatılır
            board.exit()
             
    
    def otomatikKlima(self):
        
        data=self.sensorDeger()   #sensörden değer alma 
        tahmin=ML.TahminAlgorit(data[0], data[1])  #tahmin algoritmasına sıcaklık ve nem değerlerini gönderme
        if(tahmin==1):
            self.klimaIslemi(1)  
            return 1
        else:
            self.klimaIslemi(0)
            return 0
            
            
            
            
            
            
            
            
            
            
            

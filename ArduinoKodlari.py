

class RobotikIslem():
    
    def __init__(self):
        
        self.port = 'COM4'
        self.board = Arduino(port)
        
    def sensorDeger(self):
        dht_pin = 2 
        dht_sensor = Adafruit_DHT.DHT11
        nem_deger, sicaklik_deger = Adafruit_DHT.read_retry(dht_sensor, dht_pin)
        return [sicaklik_deger,nem_deger]

    def klimaIslemi(self,durum):
        self.board.get_pin("d:7:o") #klima bağlı pin
        if(durum):
             board.digital[7].write(1)
             board.exit()
        else:
            board.digital[pin_numarasi].write(0)
            board.exit()
             
    
    def otomatikKlima(self):
        
        data=self.sensorDeger()
        tahmin=ML.TahminAlgorit(data[0], data[1])
        if(tahmin==1):
            self.klimaIslemi(1)
            return 1
        else:
            self.klimaIslemi(0)
            return 0
            
            
            
            
            
            
            
            
            
            
            

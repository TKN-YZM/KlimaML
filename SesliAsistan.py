import random
import time
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import pyaudio
import os
import ArduinoKodlari 
import VeriTabani


r=sr.Recognizer()
rbt=ArduinoKodlari.RobotikIslem()
db=VeriTabani.DataBase()

class SesliAsistan:

    def seslendirme(self, metin):
        metin_seslendirme = gTTS(text=metin, lang="tr")
        dosya = str(random.randint(0, 10000000000)) + ".mp3"
        metin_seslendirme.save(dosya)
        playsound(dosya) 
        os.remove(dosya)

    def mikrofon(self):
        
        with sr.Microphone() as kaynak:
            print("Sizi dinliyorum..")
            listen=r.listen(kaynak)
            ses=""
            try:
                ses=r.recognize_google(listen,language="tr-TR")
            except sr.UnknownValueError:
                self.seslendirme("ne dediğinizi anlayamadım")
            return ses.lower()

    def sesKarslik(self,gelen_Ses):
        
        if gelen_Ses in "klimayı aç":  
            self.seslendirme("Klimanızı hemen açıyorum...")
            rbt.klimaIslemi(1) #klima açma
            data=rbt.sensorDeger() #DHT11 sensöründen nem ve sıcaklık değerleri 
            sicaklik_deger=data[0] #sıcaklık değer
            nem_deger=[1]          #nem değer
            db.veriEkle(sicaklik_deger, nem_deger, 1) #veri tabanına arka planda kayıt
        
        elif gelen_Ses in "klimayı kapat":
            self.seslendirme("klimanızı kapatıyorum...")
            rbt.klimaIslemi(0)
    
    
    
    

    def uyanmaFonksiyonu(self,gelen_Ses):
        if(gelen_Ses in "hey siri"):
            self.seslendirme("dinliyorum...")
            ses=self.mikrofon()
            if(ses!=""):
                print(ses)
                rbt.otomatikKlima() #makine kendi karar verecek
                self.sesKarslik(ses)



asistan = SesliAsistan()

while True:
    gelen_Ses=asistan.mikrofon()
    if(gelen_Ses!=""):
        print(gelen_Ses)
        
        asistan.uyanmaFonksiyonu(gelen_Ses)


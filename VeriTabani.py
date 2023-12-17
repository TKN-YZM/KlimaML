import sqlite3
import pandas as pd
    
class DataBase:
    
    def __init__(self):
        #veri tabanı python bağlantıları
        self.conn=sqlite3.connect("KlimaVerileri.db")
        self.cursor=self.conn.cursor()
        self.__tabloOlustur()
   
        
    def __tabloOlustur(self):
        #veri tabanı yoksa oluşturma
        self.cursor.execute("Create Table if not exists KlimaTablo (Sıcaklık Real,Nem Real,KlimaAcik Int)")
        self.conn.commit()
  
        
    def veriEkle(self,sicaklik: float,nem: float,klima_acik: int):
        
        data=self.veriTabaniGetir() #tüm veriler
        flag=False
        print(data)
        
        for indeks,satir in data.iterrows(): #tablo verilerini parçala
            sicaklik_tablo=satir["Sıcaklık"]
            nem_tablo=satir["Nem"]
            durum_tablo=satir["KlimaAcik"]
            
            #aynı veri varsa overfitting riski sebebiyle ekleme yapmıyoruz
            if(sicaklik_tablo==sicaklik and nem_tablo==nem and durum_tablo==klima_acik): 
                flag=True
         
                
        if(flag==False):
             print("Data eklendi")
             x="Insert into KlimaTablo Values (?,?,?)"
             self.cursor.execute(x,(sicaklik,nem,klima_acik))
             self.conn.commit() 
            
        
    def veriGoster(self):
        #tüm verilerin getirilmesi  / proje aşamasında verilerin gözetilmesi için oluşturulmuş hazır fonksiyon
        self.cursor.execute("Select * from KlimaTablo")
        liste=self.cursor.fetchall()
        print("Sıcaklık |Nem |Klima Durumu")
        for x in liste:
            print(x )
        self.conn.commit()
       
        
    def veriTabaniGetir(self):
        sql_query = "SELECT * FROM KlimaTablo;"
        conn=sqlite3.connect("KlimaVerileri.db")
        
        data = pd.read_sql(sql_query, conn)
        
        return data
        
    

     


    

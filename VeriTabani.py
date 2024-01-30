import sqlite3
import pandas as pd
    
class DataBase:
    
    def __init__(self):
        self.conn=sqlite3.connect("KlimaVerileri.db")
        self.cursor=self.conn.cursor()
        self.__tabloOlustur()

    def __tabloOlustur(self):
        
        self.cursor.execute("Create Table if not exists KlimaTablo (Sıcaklık Real,Nem Real,KlimaAcik Int)")
        self.conn.commit()

    def veriEkle(self,sicaklik: float,nem: float,klima_acik: int):
        
        data=self.veriTabaniGetir() #tüm veriler
        flag=False
        print(data)
        
        for indeks,satir in data.iterrows(): #tablo verilerini aparçala
            sicaklik_tablo=satir["Sıcaklık"]
            nem_tablo=satir["Nem"]
            durum_tablo=satir["KlimaAcik"]
            
            #aynı veri varsa overfitting riski sebebiyle ekleme yapmıyoruz
            if(sicaklik_tablo==sicaklik and nem_tablo==nem and durum_tablo==klima_acik): 
                flag=True

        if(flag==False):
             x="Insert into KlimaTablo Values (?,?,?)"
             self.cursor.execute(x,(sicaklik,nem,klima_acik))
             self.conn.commit()
             print("Data eklendi")


    def veriGoster(self):
        self.cursor.execute("Select * from KlimaTablo")
        liste=self.cursor.fetchall()
        print("Sıcaklık |Nem |Klima Durumu")
        for x in liste:
            print(x )
        self.conn.commit()

    def veriTabaniGetir(self):
        sql_query = "SELECT * FROM KlimaTablo;"
        data = pd.read_sql(sql_query, self.conn)
        return data



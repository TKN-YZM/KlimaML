import pandas as pd
import numpy as np
import sqlite3
import VeriTabani as DB
from sklearn.metrics import confusion_matrix #Performans ölçümü
from sklearn.linear_model import LogisticRegression  #ML Algoritması
from sklearn.model_selection import GridSearchCV  #En optimum parametre 
from sklearn.model_selection import train_test_split 


class MakineAlgorit():
    
    def __init__(self):
        
        self.db=DB.DataBase()
        self.data=self.db.veriTabaniGetir()  #Tüm verilerin getirilmesi
        sicaklik_nem=self.data[["Sıcaklık","Nem"]] 
        klima_deger=self.data[["KlimaAcik"]]
        print(self.data.corr()) #Veriler arası korelasyon gözetme
        self.x_Train,self.x_Test,self.y_Train,self.y_Test=train_test_split(sicaklik_nem,klima_deger,random_state=2,test_size=0.2)
    
    #Algoritamanın öğrenim/tahmin yüzdeliği
    def __matrixOran(self,true_table,predict_table):
        
         if isinstance(true_table, pd.DataFrame):
            cf=confusion_matrix(true_table,predict_table)
            print(cf)
            #True Positive  ---
            tp = cf[1, 1]   
            # False Positive (FP)
            fp = cf[0, 1]
            # True Negative (TN) --
            tn = cf[0, 0]
            # False Negative (FN)
            fn = cf[1, 0]
            istatistic=(tp+tn)/(tp+fp+tn+fn)*100
            print("İstatistik: ",istatistic)
            return (tp+tn)/(tp+fp+tn+fn)*100
    
         else:
            print("Hata: Geçerli bir tablo verisi bekleniyor.")

    
    #Parametre Optimizasyonunun yapılması (GridSearch ile)
    def __parametreOptim(self,clsfr,p: list):
        
        #p=[{'n_neighbors':[2,3,4,5,6,7,8,9,10],'metric':['minkowski']}]    
    
        gs=GridSearchCV(estimator=clsfr, param_grid=p,scoring='accuracy',cv=10,n_jobs=-1)
        
        grid_searc=gs.fit(self.x_Train, self.y_Train)
        
        eniyi_sonuc=grid_searc.best_score_
        
        eniyi_param=grid_searc.best_params_
        
    
        print("Algoritmasının Optimum Parametreleri: ")
        for key,value in eniyi_param.items():
            print(f'Değişken: {key}  Optimum Değer: {value}')
        
    #LogisticRegression kullanımı
    def TahminAlgorit(self,sicaklik_deg:int,nem_deger:int):
        
        lg=LogisticRegression(solver='newton-cg')
        lg.fit(self.x_Train,self.y_Train)
        predict=lg.predict(self.x_Test)
        
        self.__matrixOran(self.y_Test, predict)
        
        '''
            print("LG OPTIMUM")
            parametreOptim(lg, [{'solver':['newton-cg', 'lbfgs', 'liblinear', 'sag']}])
        '''
        
        return lg.predict([[sicaklik_deg,nem_deger]])
       



sayi1 = int(input ("Kaç dolar?"))
class kurCevir:
    def carp (self,sayi1,sayi2):
        return sayi1 * sayi2

kur = kurCevir ()
sonuc = kur.carp(sayi1,8)
print("TL karşılığı",sonuc)



donusumorani = 7.8
TL= int (input ("kac"))
dolar= TL* donusumorani
print (str (TL)+ "TL" + str (dolar) + "eder")

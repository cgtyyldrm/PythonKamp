sehirler = ["ankara", "istanbul", "izmir"]
for sehir in sehirler:
    print(sehir)
for sayi in range (10):
    print (sayi)
for sayi in range (1,10): #1'den 10'a kadar
    print (sayi*"a")
for sayi in range (1):
    print (*range (0,10,2)) #0'dan 10 a kadar 2'şerli, çift sayılar
sayi = 1
while sayi <=10:
    print (sayi)
    sayi = sayi +1

isim = input ("adiniz")
print ("isim:" + isim)

sayi = int (input ( "sayi:"))
faktoriyel = 1
sayi = int (input ("kacin faktöreyileni hesaplayalım:"))
#5 faktoriyel =120
#0'ın faktoriyeli hesaplanmaz
if sayi < 0:
    print ("negatif sayilerin faktoriyeli hesaplanmaz")
elif  sayi == 0:
    print ("sonuc: 1")
else:
    for i in range (1, sayi +1):
        faktoriyel = faktoriyel *i
    print ("sonuc:", faktoriyel)
    
#kullanıcı 3 sayı girsin bunlardan en büyüğünü versin
sayi1 = int(input ("sayi 1:"))
sayi2 = int(input ("sayi 2:"))
sayi3 = int(input ("sayi 3:"))

if sayi1>sayi2 and sayi1>sayi3:
    print ("en büyük sayi1")
elif sayi2>sayi1 and sayi2>sayi3:
    print ("en büyük sayi2")
elif sayi3>sayi1 and sayi3>sayi2:
    print ("en büyük sayi 3. sayı olan", sayi3)
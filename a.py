sayi=int(input("Faktoriyeli alınacak sayıyı giriniz : "))
carpim=1

for i in range(sayi):
    carpim*=i+1
    print(carpim)
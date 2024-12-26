import random
karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Kaç karakterlik bir şifre olsun"))
sifre = ""
for i in range(uzunluk):
    sifre += random.choice(karakter)
print(sifre)
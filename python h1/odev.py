ad = input("Adınızı girin: ")
yas = int(input("Yaşınızı girin: "))
dogum_yili = int(input("Doğum yılınızı girin: "))

print(f"Merhaba {ad}! {yas} yaşındasın ve {dogum_yili} yılında doğmuşsun.")


sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

toplam = sayi1 + sayi2
fark = sayi1 - sayi2
carpim = sayi1 * sayi2
bolum = sayi1 / sayi2

print(f"{sayi1} + {sayi2} = {toplam}")
print(f"{sayi1} - {sayi2} = {fark}")
print(f"{sayi1} * {sayi2} = {carpim}")
print(f"{sayi1} / {sayi2} = {bolum}")
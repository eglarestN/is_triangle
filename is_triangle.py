# Ad Soyad = Muhammed Emir Yıldırım

# rastgele sayılar üretmesi için random modülünü kullanırım
import random
# gecen sureyi hesaplaması için time modülünü kullanırım
import time

baslama_zamani = time.time()

ucgen_sayisi = 0
deneme = 1000000

# kaç adet ücgen oluştuğunu öğrenmek için for döngüsü kullanırım
for num in range(deneme):

# random modülü ile iki adet rastgele nokta alırım
    nokta1 = random.uniform(0, 100)
    nokta2 = random.uniform(0, 100)

#Cubugu 3 parcaya ayırırım
    parca1 = abs(nokta1 - nokta2)

    if nokta1 < nokta2:
        parca2 = nokta1
    else:
        parca2 = nokta2

    if nokta1 > nokta2:
        parca3 = 100 - nokta1
    else:
        parca3 = 100 - nokta2

# ayrılan kenarların üçgen oluşturma kurallarına göre üçgen oluşturup oluşturulmadığını kontrol ederim
    if parca1 + parca2 > parca3 and parca1 + parca3 > parca2 and parca2 + parca3 > parca1:
        ucgen_sayisi += 1

bitis_zamani = time.time()
gecen_sure = bitis_zamani - baslama_zamani
basari_orani = ucgen_sayisi / deneme

print(f"1.000.000 denemede {ucgen_sayisi} sayida ücgen %{basari_orani} basari ile {gecen_sure} saniyede olustu")








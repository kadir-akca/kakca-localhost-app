import random
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    input("bisey yaz")
    return "test"


def oyun_1():
    print("0-100 arasindaki sayiyi tahmin et!")
    rand_number = random.randint(0, 100)
    tahmin = 0
    while 1:
        user_input_number = input("1.Tahmin:")
        if int(user_input_number) == rand_number:
            tahmin = tahmin + 1
            print("Dogru sayiyi buldun, Kadion seni tebrik eder! \n" + str(tahmin) + ". denemede buldun!")
            break
        elif int(user_input_number) < rand_number:
            tahmin = tahmin + 1
            print("Cik yukari! Daha yüksek!")
        elif int(user_input_number) > rand_number:
            tahmin = tahmin + 1
            print("Asagi in! Daha düsük!")


def oyun_2():
    print("Carpim oyununa hosgeldin!\n 10 tane soruyu Kadion sana soracak, bakalim kac tane bileceksin!")
    soru_sayi = 0
    dogru_sayisi = 0
    while 1:
        rand_1 = random.randint(0, 10)
        rand_2 = random.randint(0, 10)
        soru_sayi = soru_sayi + 1
        sonuc = rand_1 * rand_2
        print(rand_1, rand_2)
        user_input_number = input("Yukaridaki iki sayinin carpimi kactir?")
        if soru_sayi == 10:
            print("   " + str(dogru_sayisi) + "/10 dogru cevaba ulastin!\n     Kadion sana mutlu günler diler!")
            break
        elif int(user_input_number) != sonuc:
            print("Yanlis cevap! Kadion kizgin!")
            continue
        elif int(user_input_number) == sonuc:
            dogru_sayisi = dogru_sayisi + 1
            print("Aferin! Dogru Cevap!")
            print("Siradaki...")


def oyun_3():
    print("Dikey ve capraz yazdir oyununa hosgeldin " + kullanici_isim + "!")
    while 1:
        user_input = input("Bir kelime gir: ")
        lenght = len(user_input) - 1
        bosluk1 = ""
        bosluk2 = lenght * "  "
        print(lenght)
        for letter in user_input:
            print(letter)
        print("")
        for letter in user_input:
            print(bosluk1 + letter)
            bosluk1 = bosluk1 + "  "
        print("")
        for letter in user_input:
            print(bosluk2 + letter)
            lenght = lenght - 1
            bosluk2 = lenght * "  "


def oyun_4():
    print("Kelimemi tahmin et oyununa hos geldin " + kullanici_isim + "\nBu oyun iki kisiliktir.")
    tahmin_edilecek_kelime = input(kullanici_isim +
                                   ", arkadasinin tahmin etmesini istedigin bir kelime yaz: ")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    harf_sayisi = len(tahmin_edilecek_kelime)
    yeni = tahmin_edilecek_kelime.replace(tahmin_edilecek_kelime, harf_sayisi * "_")
    while 1:
        if yeni == tahmin_edilecek_kelime:
            print("Tebrikler kardes!")
            break
        tekrar_engel = 0
        harf = input("Harf gir: ")
        for harfler in tahmin_edilecek_kelime:
            if harf == harfler:
                harf_yeri = [pos for pos, char in enumerate(tahmin_edilecek_kelime) if char == harf]
                for j in harf_yeri:
                    matris_uzunluk = len(harf_yeri)
                    pozisyon = j
                    yeni = yeni[:pozisyon] + harf + yeni[(pozisyon + 1):]
                    tekrar_engel = tekrar_engel + 1
                    if tekrar_engel == matris_uzunluk:
                        print(yeni)
        print("Bu harfleri söyledin: " + harf)


def oyun_5():
    print("Ortalama bulma aracina hos geldin " + kullanici_isim +
          "\nIstedigin kadar sayi girdikten sonra tüm bu sayilarin ortalamasini görmek icin 'tamam' yaz.")
    sayi_listesi = list()
    while 1:
        sayi = input("Sayi gir:")
        if sayi == "tamam":
            break
        fsayi = float(sayi)
        sayi_listesi.append(fsayi)
    ortalama = sum(sayi_listesi) / len(sayi_listesi)
    print("Iste girdigin sayilarin ortalamasi:", ortalama)


print("\n")

print("Hos geldin degerli kullanici, "
      "\nKadion seni daha yakindan tanimak ister!"
      "\n\n ")

kullanici_isim = input("Adin nedir: ")
print("\n")
print("Tekrar hos geldin " + kullanici_isim + "!!!" "\nHangi oyunu oynamak istersin " + kullanici_isim + "?")
print("      1.'Random sayiyi tahmin et!' oyunu")
print("      2.'Matematik carpim' oyunu")
print("      3.'Girdigin kelimeyi yatay yazdir!' oyunu")
print("      4.'Kelimemi tahmin et!' oyunu")
print("      5.'Girdigin sayilarin ortalamasini bul!' oyunu")


print("\n")
mod = input("Lütfen bir oyun sec:")

if int(mod) == 1:
    oyun_1()

elif int(mod) == 2:
    oyun_2()

elif int(mod) == 3:
    oyun_3()

elif int(mod) == 4:
    oyun_4()

elif int(mod) == 5:
    oyun_5()

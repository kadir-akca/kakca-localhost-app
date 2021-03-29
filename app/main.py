import random
from flask import Flask
app= Flask(__name__)
@app.route('/')

def index():
    print("\n")
    print("Hos geldin degerli kullanici, "
          "\nKadion seni daha yakindan tanimak ister!"
          "\n\n ")

    kullanici_isim = input("Adin nedir: ")
    print("\n")
    print("Tekrar hos geldin " + kullanici_isim + "!!!" "\nHangi oyunu oynamak istersin " + kullanici_isim + "?"
                                                                                                             "\n"
                                                                                                             "\n      1.'Random sayiyi tahmin et!' oyunu"
                                                                                                             "\n      2.'Matematik carpim' oyunu"
                                                                                                             "\n      3.'Girdigin kelimeyi yatay yazdir!' oyunu"
                                                                                                             "\n      4.'Kelimemi tahmin et!' oyunu"
                                                                                                             "\n      5.'Girdigin sayilarin ortalamasini bul!' oyunu")
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

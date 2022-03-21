import os
import time


BankaAdi = "Hayat Banka"

class Musteri():
    def __init__(self, ID, ISIM, SIFRE):
        self.id = ID
        self.__ISIM = ISIM
        self.__SIFRE = SIFRE #özel bilgiler iki altçizgi iler kapsüllenir gizlenir
        self.__BAKIYE = 0

    def getISIM(self):
        return self.__ISIM

    def getSIFRE(self):
        return self.__SIFRE

    def getBAKIYE(self):
        return self.__BAKIYE

    def setBAKIYE(self, MIKTAR: int):
        self.__BAKIYE += int(MIKTAR)


class Bank():
    def __init__(self):
        self.MUSTERILER = list() #connstertır (yapıcı fonksiyon) 

    def MusteriOl(self, ID, ISIM, SIFRE):
        os.system("cls")
        self.MUSTERILER.append(Musteri(ID, ISIM, SIFRE)) # müşteriler listesine nesene ekliyoz
        print("""
        -- ==  {} HOŞGELDİNİZ  == --

        Merhaba, {}
        Müsteri Numaranız (ID):  {}
        Şifreniz:  {}
        """.format(BankaAdi, ISIM, ID, len(SIFRE) * "*"))#.format paratezler içine yerleştirilir f string gibi

        input("Lütfen herhangi bir tuşa basınız..")


def Main():
    
    sayac_ID = 0 # geçici değişken
    sayac_Quit = False # geçici değişken
    bank = Bank() #banka nesnesi yarattık

    while True:
        sayac_Quit = False
        os.system("cls") #konsol ekranını temizleme
        print("Hoşgeldiniz, {}!".format(BankaAdi))
        print("=" * (14 + len(BankaAdi)), "\n")  # düzrn görsel = ekleme
        print("""
[1]: Müşteriyim
[2]: Müşteri olmak istiyorum
        """)

        secim_1 = input("Lütfen bir işlem giriniz => ")

        if secim_1 == "1":
            ids = [i.id for i in bank.MUSTERILER] #  MUSTERIELERIN IDLERI uzun hali program bsalamadan id leri göndeiyorsun
            
            # ids = []
            # for i in bank.MUSTERILER:
            #    ids.append(i.id)
                
                
            os.system("cls")
            
            
            while True:
                if sayac_Quit == True: #öyle ise döngüyüyü kır 
                    break
                TryID = input("Kayit icin bir Müsteri Numarası (ID) seciniz : ")
                if TryID in ids:#müşteri müşteri ise
                    sayac_ID = 0
                    for Musteri in bank.MUSTERILER:
                        if Musteri.id == TryID: # kontrol
                            TrySIFRE = input("Şifrenizi girin: ")
                            if TrySIFRE == Musteri.getSIFRE(): # kontrol
                                while True:
                                    os.system("cls")
                                    print("Hoşgeldiz, {}!".format(Musteri.getISIM()))
                                    print((10 + len(Musteri.getISIM())) * "=", "\n")
                                    print("""
                                    [1]: Bakiyem ne kadar?
                                    [2]: Hesabıma para yatır
                                    [3]: Başka bir hesaba para yatır
                                    [4]: Para Çek
                                    [0]: Çıkış
                                    """)
                                    secim_2 = input("Lütfen bir işlem giriniz => ")
                                    if secim_2 == "0": # çıkış
                                        os.system("cls")
                                        print("Bizi seçtiğiniz için teşekkürler! Hoşçakalın!")
                                        input("Lütfen herhangi bir tuşa basınız..")
                                        sayac_Quit = True
                                        break
                                    elif secim_2 == "1":  # bakiyem ne kadar
                                        os.system("cls")
                                        print("Merhaba! {}".format(Musteri.getISIM()))
                                        print("Bakkiyeniz: $ {}".format(Musteri.getBAKIYE()))
                                        input("Lütfen herhangi bir tuşa basınız..")
                                    elif secim_2 == "2":  # hesaba para yatırma
                                        os.system("cls")
                                        print("Merhaba!, {}".format(Musteri.getISIM()))
                                        MIKTAR = int(input("Lütfen Miktarı giriniz: "))
                                        print("Önceki bakiyeniz: $ {}".format(Musteri.getBAKIYE()))
                                        Musteri.setBAKIYE(MIKTAR)
                                        print("Şimdiki bakiyeniz: $ {}".format(Musteri.getBAKIYE()))
                                        input("Lütfen herhangi bir tuşa basınız..")
                                    elif secim_2 == "3":  # başka hesaba para yatırma
                                        os.system("cls")
                                        print("Merhaba! {}".format(Musteri.getISIM()))
                                        digerID = input("Müsteri Numarasını (ID) girin: ") #yatıracağımız müşterinin numarası
                                        if digerID in ids:
                                            for digerID2 in bank.MUSTERILER:
                                                if digerID == digerID2.id:
                                                    MIKTAR = input("Miktarı giriniz: ")
                                                    if int(MIKTAR) > int(Musteri.getBAKIYE()):
                                                        print("Yeteri kadar bakiyen yok.")
                                                        input("Lütfen herhangi bir tuşa basınız..")
                                                    else:
                                                        os.system("cls")
                                                        print("Transfer Başarılı!")
                                                        print("Önceki BAKIYE $ {}".format(Musteri.getBAKIYE()))
                                                        Musteri.setBAKIYE(-int(MIKTAR))
                                                        digerID2.setBAKIYE(+int(MIKTAR))
                                                        print("Şu anki BAKIYE $ {}".format(Musteri.getBAKIYE()))
                                                        input("Lütfen herhangi bir tuşa basınız..")
                                        else:
                                            print("Bu müşteri numarası(ID) bulunamadı.")
                                            input("Lütfen herhangi bir tuşa basınız..")
                                            continue
                                    elif secim_2 == "4":  # para çekme
                                        os.system("cls")
                                        MIKTAR = input("Lütfen miktarı girin: ")
                                        if int(MIKTAR) > int(Musteri.getBAKIYE()):
                                            print("Yeteri kadar bakiyen yok.")
                                            input("Lütfen herhangi bir tuşa basınız..")
                                        else:
                                            print("Çekilen para: ${}".format(MIKTAR))
                                            print("Önceki BAKIYE $ {}".format(Musteri.getBAKIYE()))
                                            Musteri.setBAKIYE(-int(MIKTAR))
                                            print("Şimdiki BAKIYE $ {}".format(Musteri.getBAKIYE()))
                                            input("Lütfen herhangi bir tuşa basınız..")
                            else:
                                print("SIFRE Yanlıs, Lütfen tekrar deneyiniz.")
                                input("Lütfen herhangi bir tuşa basınız..")

                else:  #deneme hakkı yanlış girilir ise 3 hak verir
                    sayac_ID += 1
                    if sayac_ID >= 3:
                        print("Lütfen Sonra tekrar deneyiniz.")
                        time.sleep(2)# iki saniye beklet
                        sayac_ID = 0
                        break

                    else:
                        print("Bu müşteri numarası(ID) bulunamadı.")
                        input("Lütfen herhangi bir tuşa basınız..")




        elif secim_1 == "2":
            os.system("cls")
            print("Merhaba, sizi aramızda göreceğimizden mutluyuz!")
            print("""                    ===""")
            ids = [i.id for i in bank.MUSTERILER]

            ID = input("Lütfen bir müsteri numarası (ID) seçiniz => ")

            if ID in ids:
                print("Bu müsteri numarası kullanılıyor.")
                input("Lütfen herhangi bir tuşa basınız..")
            else:
                ISIM = input("İsminiz Nedir? => ")
                SIFRE = input("SIFRE Belirleyin => ")
                print("")
                bank.MusteriOl(ID, ISIM, SIFRE)


        else:
            print("Yanlış Tuşladınız! Lütfen Tekrar Deneyin.")
            input("Lütfen herhangi bir tuşa basınız..")


if __name__ == '__main__':
    Main()

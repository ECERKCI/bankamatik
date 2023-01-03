#Bankamatik Uygulaması
EceHesap = {
    'ad': 'Ece ERKCİ',
    'hesapNo': '12345678',
    'bakiye': 3000,
    'ekHesap': 2000
}
AnilHesap = {
    'ad': 'Anil ERKCİ',
    'hesapNo': '12347589',
    'bakiye': 2000,
    'ekHesap': 1000
}
 
def paraCek (hesap,miktar):
    print(f"merhaba{hesap['ad']}")
    if (hesap['bakiye'])>= miktar:
      print('paranızı alabilirsiniz.')
    else:
        toplam= help ['bakiye']+ hesap['ekHesap']
        if (toplam>= miktar):
             ekHesapKullanımı=input('ek hesap kullanılsın mı(e/h)')
             if ekHesapKullanımı=='e':
                print('paranızı alabilirsiniz.')
             else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print('üzgünüz bakiye yetersiz.')


paraCek(EceHesap,2000)    
print('Pilih salah satu kategori di bawah: ')
print('1. Luas Segitiga')
print('2. Luas Persegi')
print('3. Jajargenjang')
pil = input('Masukkan pilihan: ')

def luas(pil):
    if(pil == '1'):
        print("Luas Segitiga")
        alas = input("Masukkan alas: ")
        tg = input("Masukkan Tinggi :")
        luas = float(alas)*float(tg)/2
        print("Luas segitiga: "+str(luas))
    elif(pil =='2'):
        print("Luas Persegi")
        sisi = input("Masukkan sisi: ")
        luas = float(sisi)*float(sisi)
        print("Luas Persegi: "+str(luas))
    elif(pil=='3'):
        print("Luas Jajargenjang")
        alas = input("Masukkan Alas: ")
        tg = input("Masukkan tinggi: ")
        luas = float(alas)*float(tg)
        print("Luas jajar genjang: "+str(luas))
luas(pil)
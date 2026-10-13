#tugas no1
kendaraan = ["vario", "motor", 150, "biru", 2]
tambahan = [25000000, "matic"]
kendaraan.extend(tambahan)
kendaraan.insert(2, "honda")
print(kendaraan)



#tugas no2
print("=== Alat hitung luas bangun datar ===")
print("Pilih 1 untuk menghitung luas persegi")
print("Pilih 2 untuk menghitung luas lingkaran")
print("Pilih 3 untuk menghitung luas segitiga")

Pilihan = int(input("Masukkan pilihan (1/2/3): "))

match Pilihan:
    case 1:
        s = int(input("Masukkan panjang sisi persegi: "))
        luas = s * s
        print(f"Luas persegi adalah: {luas}")
        
    case 2:
        r = int(input("Masukkan jari jari lingkaran: "))
        pi = 3.14
        luas = pi * r**2
        print(f"Luas lingkaran adalah: {luas}")
       
    case 3:
         a = int(input("Menghitung panjang alas segitiga: "))
         t = int(input("Masukkan panjang tinggi segitiga: "))
         luas = a * t / 2
         print(f"Luas segitiga adalah: {luas}")
           
    case _:
            print("Masukkan pilihan dengan benar")
           
#soal 2


print("Program Menghitung Luas Bangun Datar")
print("1. Persegi")
print("2. Lingkaran")
print("3. Segitiga")

hitung = int(input("memilih program (1/2/3): "))

match hitung:
    case 1:
         sisi = float(input("Masukan panjang sisi: "))
         luas = sisi * sisi
         print(luas)
    case 2:
         r = float(input("Masukan jari-jari lingkaran: "))
         luas = 3.14 * r * r
         print(luas)
    case 3:
         alas = float(input("Masukan alas segitiga: "))
         tinggi = float(input("Masukan tinggi segitiga: "))
         luas = 0.5 * alas * tinggi
         print(luas)
    case _:
         print("SALAH PILIH")
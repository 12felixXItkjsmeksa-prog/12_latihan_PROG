import ganjil_genap
while True:
  angka = int(input("masukkan sebuah angka: "))

#memanggil fungsi file ganjil_genap.py
ganjil_genap.cek_ganjil_genap(angka)

pilihan = input("apakah ingin lanjut y/n: ").lower()
if plihan == 'n':
  print("progam selesai. terimakasih.")
  break

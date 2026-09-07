import ganjil_genap
import urllib.request
import csv

# Pastikan link diawali dengan https:// dan diakhiri dengan output=csv
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTBKd3Wj5AWiaaE8O1Pfw6hoPfdw5tCBh8XIeccyLFOt-z6H0p7klVx1org5qxGN4jg05AQKBuN0EbA/pub?output=csv"

def load_users():
    users = {}
    try:
        req = urllib.request.Request(CSV_URL, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        lines = [line.decode('utf-8') for line in response.readlines()]
        reader = csv.reader(lines)
        next(reader, None)  # Melewati baris header (username, password)
        for row in reader:
            if len(row) >= 2:
                users[row[0].strip()] = row[1].strip()
    except Exception as e:
        print("Gagal membaca dari Google Sheets, menggunakan data cadangan.")
        users = {"admin": "01052010"}
    return users

# Mengambil data user langsung dari Google Sheets
users_db = load_users()

print("=== HALAMAN LOGIN ===")
username = input("masukkan username: ")
password = input("masukkan password: ")

if username in users_db and users_db[username] == password:
    print("login berhasil!\n")
    while True:
        angka = int(input("masukkan sebuah angka: "))
        
        # memanggil fungsi file ganjil_genap.py
        ganjil_genap.cek_ganjil_genap(angka)
        
        pilihan = input("apakah ingin lanjut y/n: ").lower()
        if pilihan == 'n':
            print("progam selesai. terimakasih.")
            break
else:
    print("Login gagal! Username atau password salah.")

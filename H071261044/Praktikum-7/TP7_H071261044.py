import os
import random
from datetime import datetime

FOLDER = "invoices"
FILE_RIWAYAT = "try_history.txt"

#Membuat folder invoice yang belum ada
if not os.path.exists(FOLDER):
    os.mkdir(FOLDER)

def input_angka(pesan, minimal):
    while True:
        try:
            angka = int(input(pesan))
        except ValueError:
            print("Input harus berupa angka!")
            continue

        if angka < minimal:
            print(f"Input tidak boleh kurang dari {minimal}!")
        else:
            return angka

def buat_id(nama_kasir, waktu):
    inisial = ""
    for kata in nama_kasir.split():
        inisial += kata[0].upper()

    tanggal_waktu = waktu.strftime("%y%m%d%H%M")
    acak = random.randint(100, 999)
    return inisial+ tanggal_waktu + str(acak)

def simpan_riwayat(waktu, id_transaksi, total):
    garis = "=" * 61

    # Kalau file belum ada, tulis dulu judul tabelnya
    if not os.path.exists(FILE_RIWAYAT):
        with open(FILE_RIWAYAT, "w") as file:
            file.write(garis + "\n")
            file.write("| " + "RIWAYAT TRANSAKSI".center(57) + " |\n")
            file.write(garis + "\n")
            file.write("| " + "Waktu".center(14) + " | " + "ID Transaksi".center(20) + " | " + "Nominal Transaksi".center(17) + " |\n")
            file.write(garis + "\n")

    # Tambahkan 1 baris untuk transaksi ini
    with open(FILE_RIWAYAT, "a") as file:
        w = waktu.strftime("%d/%m/%y %H:%M")
        nominal = "Rp" + str(total)
        file.write("| " + w.ljust(14) + " | " + id_transaksi.ljust(20) + " | " + nominal.rjust(17) + " |\n")
        file.write(garis + "\n")

def transaksi_baru(nama_kasir):
    # ---------- Input produk ----------
    keranjang = [] 

    while True:
        print("=" * 50)
        nama = input("Masukkan nama produk     : ")
        harga = input_angka("Masukkan harga produk    : ", 0)
        jumlah = input_angka("Masukkan jumlah produk   : ", 1)

        keranjang.append({"nama": nama, "harga": harga, "jumlah": jumlah})

        print("=" * 50)
        lagi = input("Tambah produk? (y/t)     : ")
        if lagi.lower() != "y":
            break

    # ------------ Menyusun ID dan hitung total ---------
    waktu = datetime.now()
    id_transaksi = buat_id(nama_kasir, waktu)

    total = 0
    for produk in keranjang:
        total += produk["harga"] * produk["jumlah"]

    # ----------- Menulis Invoice ke file.txt -----------
    path = os.path.join(FOLDER, id_transaksi + ".txt")
    garis_tabel = "  " + "=" * 55 + "\n"

    with open(path, "w") as file:
        file.write("\n")
        file.write("TOKO ZERO".center(60, "=") + "\n")
        file.write("\n")
        file.write("=" * 60 + "\n")
        file.write("Nama kasir      : " + nama_kasir + "\n")
        file.write("Waktu transaksi : " + waktu.strftime("%d/%m/%y %H:%M") + "\n")
        file.write("=" * 60 + "\n")
        file.write("\n")
        file.write("Daftar Produk".center(60, "-") + "\n")
        file.write("\n")
        file.write(garis_tabel)
        file.write("  | " + "Nama".center(17) + " | " + "Harga".center(9) + " | " + "Jumlah" + " | " + "Total".center(10) + " |\n")
        file.write(garis_tabel)

        for produk in keranjang:
            nama = produk["nama"]
            if len(nama) > 17:
                nama = nama[:14] + "..."     # potong nama yang kepanjangan
            harga = "Rp" + str(produk["harga"])
            jumlah = str(produk["jumlah"])
            subtotal = "Rp" + str(produk["harga"] * produk["jumlah"])
            file.write("  | " + nama.ljust(17) + " | " + harga.rjust(9) + " | " + jumlah.center(6) + " | " + subtotal.rjust(10) + " |\n")

        file.write(garis_tabel)
        file.write("  | " + "TOTAL".center(38) + " | " + ("Rp" + str(total)).rjust(10) + " |\n")
        file.write(garis_tabel)
        file.write("\n")
        file.write("=" * 60 + "\n")
        file.write("TERIMA KASIH TELAH BERBELANJA".center(60, "=") + "\n")
        file.write("=" * 60 + "\n")
        
    # ----------------- Mencatat ke riwayat ------------
    simpan_riwayat(waktu, id_transaksi, total)

    print("\nTransaksi berhasil!")
    print("Invoice tersimpan dengan ID:", id_transaksi) 

# ---------- Mencari invoice ----------
def cari_invoice():
    print("=" * 50)
    id_transaksi = input("Masukkan ID transaksi    : ").strip()
    path = os.path.join(FOLDER, id_transaksi + ".txt")

    if os.path.exists(path):
        print()
        print("-" * 60)
        with open(path, "r") as file:
            print(file.read())
        print("-" * 60)
        print()
    else:
        print("=" * 50)
        print("INVOICE TIDAK DITEMUKAN".center(50))
        print("=" * 50)

# ---------- Program utama ----------
print("=" * 50)
print("SELAMAT DATANG".center(50))
print("=" * 50)

nama_kasir = input("Masukkan nama kasir      : ")
while nama_kasir.strip() == "":
    nama_kasir = input("Masukkan nama kasir      : ")
print("=" * 50)

while True:
    print("Pilih opsi:")
    print("1. Transaksi baru")
    print("2. Cari transaksi")
    print("3. Keluar")
    print("=" * 50)
    pilihan = input("Masukkan opsi pilihan    : ")

    if pilihan == "1":
        transaksi_baru(nama_kasir)
    elif pilihan == "2":
        cari_invoice()
    elif pilihan == "3":
        print("=" * 50)
        print("SAMPAI JUMPA".center(50))
        print("=" * 50)
        break
    else:
        print("=" * 50)
        print("OPSI TIDAK VALID".center(50))
        print("=" * 50)
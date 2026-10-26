import os #interaksi dgn sistem operasi t4 kode dijalankan
import random #angka random di id transaksi
from datetime import datetime #alat utk ambil jam & tgl saat ini

garis = "=" * 50

def buat_folder():
    # membuat folder invoices, kalau sudah ada ya dibiarkan saja
    try:
        os.mkdir("invoices")
    except IOError:
        pass

def buat_id(kasir, sekarang):
    inisial = "" #string kosong utk tampubg insial
    for kata in kasir.split(): #pecah nama berdasarkan spasi
        inisial = inisial + kata[0].upper() #tempel huruf kebelakang inisial

    tahun = sekarang.strftime("%y")
    bulan = sekarang.strftime("%m")
    tanggal = sekarang.strftime("%d")
    jam_menit = sekarang.strftime("%H%M")
    acak = random.randint(100, 999) #angka acak 100-999

    return inisial + tahun + bulan + tanggal + jam_menit + str(acak)

def buat_invoice(id_trx, kasir, sekarang, daftar, total):
    waktu = sekarang.strftime("%d/%m/%y %H:%M")
    nama_file = "invoices/" + id_trx + ".txt" # / msk kedlm folder invoice

    try:
        with open(nama_file, "w") as f:
            f.write("TOKO jenn".center(50) + "\n")
            f.write(garis + "\n")
            f.write("Nama kasir      : " + kasir + "\n")
            f.write("Waktu transaksi : " + waktu + "\n")
            f.write(garis + "\n")
            f.write("Daftar Produk".center(50) + "\n")
            f.write("-" * 46 + "\n")
            f.write("| Nama            | Harga     | Jml | Total      |\n")
            f.write("-" * 46 + "\n")

            for produk in daftar: #daftar adalah list
                nama = produk[0]
                harga = produk[1]
                jumlah = produk[2]
                subtotal = harga * jumlah
                # nama yang terlalu panjang dipotong supaya tabel tetap rapi
                if len(nama) > 15:
                    nama = nama[:12] + "..."
                f.write("| " + nama.ljust(15) + " | Rp" + str(harga).ljust(7) + " | " + str(jumlah).ljust(3) + " | Rp" + str(subtotal).ljust(8) + " |\n")

            f.write("-" * 46 + "\n")
            f.write("| TOTAL" + " " * 28 + "| Rp" + str(total).ljust(8) + " |\n")
            f.write("-" * 46 + "\n")
            f.write(garis + "\n")
            f.write("TERIMA KASIH TELAH BERBELANJA".center(50) + "\n")
            f.write(garis + "\n")
    except IOError:
        print("Error: could not create file " + nama_file)

def buat_file_riwayat():
    # "x" membuat file baru, error kalau file sudah ada
    try:
        with open("trx_history.txt", "x") as f:
            f.write("=" * 66 + "\n")
            f.write("RIWAYAT TRANSAKSI".center(66) + "\n")
            f.write("=" * 66 + "\n")
            f.write("| Waktu             | ID Transaksi      | Nominal Transaksi |\n")
            f.write("=" * 66 + "\n")
    except IOError: #file sudah ada
        pass

def catat_riwayat(sekarang, id_trx, total):
    buat_file_riwayat() #cek apakah file riwayat sudah dibuat
    waktu = sekarang.strftime("%d/%m/%y %H:%M:%S")

    try:
        # "a" menambah baris baru di akhir file tanpa menghapus isi lama
        with open("trx_history.txt", "a") as f:
            f.write("| " + waktu + " | " + id_trx.ljust(17) + " | Rp" + str(total).rjust(15) + " |\n")
            f.write("=" * 66 + "\n")
    except IOError:
        print("Error: could not append to file trx_history.txt")

def transaksi_baru(kasir):
    daftar = []
    total = 0
    lagi = "y" #perulangan dibawah pasti berjalan minimal sekali

    while lagi == "y":
        nama = input("Masukkan nama produk   : ")
        harga = int(input("Masukkan harga produk  : "))
        jumlah = int(input("Masukkan jumlah produk : "))
        daftar.append([nama, harga, jumlah])
        total = total + harga * jumlah
        print(garis)
        lagi = input("Tambah produk? (y/t)    : ")
        print(garis)

    sekarang = datetime.now()
    id_trx = buat_id(kasir, sekarang)

    buat_folder()
    buat_invoice(id_trx, kasir, sekarang, daftar, total)
    catat_riwayat(sekarang, id_trx, total)

    print("TRANSAKSI BERHASIL".center(50))
    print(garis)

def cari_transaksi():
    id_trx = input("Masukkan ID transaksi : ")
    nama_file = "invoices/" + id_trx + ".txt"

    try:
        with open(nama_file, "r") as f:
            isi = f.read() #baca isi file jadi satu string
            print()
            print(isi)
    except IOError:
        print("Invoice dengan ID " + id_trx + " tidak ditemukan.")

# program utama
if __name__ == '__main__': #jika file ini(py) di jalankan langsung, maka di jalankan blok dibawah
    print(garis)
    print("SELAMAT DATANG".center(50))
    print(garis)
    kasir = input("Masukkan nama kasir : ")

    pilihan = ""
    while pilihan != "3":
        print(garis)
        print("Pilih opsi:")
        print("1. Transaksi baru")
        print("2. Cari transaksi")
        print("3. Keluar")
        print(garis)
        pilihan = input("Masukkan opsi pilihan : ")
        print(garis)

        if pilihan == "1":
            transaksi_baru(kasir)
        elif pilihan == "2":
            cari_transaksi()
        elif pilihan == "3":
            print("SAMPAI JUMPA".center(50))
            print(garis)
        else:
            print("Pilihan tidak ada, coba lagi ya.")
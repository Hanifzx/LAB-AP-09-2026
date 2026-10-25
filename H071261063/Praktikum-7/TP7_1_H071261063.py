from datetime import datetime
import random
import os

folder_saat_ini = os.path.dirname(os.path.abspath(__file__))
folder_invoices = os.path.join(folder_saat_ini, "invoices")
file_history = os.path.join(folder_saat_ini, "trx_history.txt")
os.makedirs(folder_invoices, exist_ok=True)


def membuat_invoices(kasir, data_produk):
    waktu = datetime.now()
    waktu_id = waktu.strftime("%y%m%d%H%M")
    tanggal = waktu.strftime("%d/%m/%y %H:%M")
    id_trx = kasir[:3].upper() + waktu_id + str(random.randint(100, 999))
    border = "=" * 79
    header = "|" + "Nama".center(38) + "|" + "Harga".center(14) + "|" + "Jumlah".center(8) + "|" + "Total".center(14) + "|"
    total = sum(p["Harga"] * p["Jumlah"] for p in data_produk)

    with open(os.path.join(folder_invoices, id_trx + ".txt"), "w", encoding="utf-8") as f:
        f.write(f"{'TOKO ' + kasir.capitalize():^100}\n{'=' * 100}\n")
        f.write(f"{'Nama kasir':<20}: {kasir}\n{'Waktu transaksi':<20}: {tanggal}\n{'=' * 100}\n\n\n{'Daftar Produk':^100}\n\n{border:^100}\n{header:^100}\n{border:^100}\n")

        for p in data_produk:
            subtotal = p["Harga"] * p["Jumlah"]
            baris = f"| {p['Nama']:<37}| Rp{p['Harga']:>10} |{p['Jumlah']:^8}| Rp{subtotal:>10} |"
            f.write(f"{baris:^100}\n")

        f.write(f"{border:^100}\n{'|' + 'TOTAL'.center(38) + '|'.rjust(25) + f'Rp{total}'.rjust(13) + ' |':^100}\n{border:^100}\n\n\n{'=' * 100}\n{'TERIMAKASIH TELAH BELANJA':^100}\n{'=' * 100}\n")

    if not os.path.exists(file_history):
        with open(file_history, "w", encoding="utf-8") as f:
            f.write("=" * 90)

    with open(file_history, "a", encoding="utf-8") as f:
        f.write(f"\n| {tanggal:<28}| {id_trx:<29}|{'Rp' + str(total):>26} |\n{'=' * 90}")

    print("=" * 54)
    print("TRANSAKSI BERHASIL".center(54))
    print("=" * 54)


print("=" * 54)
print("SELAMAT DATANG".center(54))
print("=" * 54)
nama_kasir = input("Masukkan nama kasir".ljust(35) + ": ")

while True:
    print("=" * 54)
    print("Pilih opsi:\n1. Transaksi baru\n2. Cari transaksi\n3. keluar")
    print("=" * 54)
    pilihan = input("Masukkan opsi pilihan".ljust(35) + ": ")
    print("=" * 54)

    if pilihan == "1":
        data_list = []

        while True:
            try:
                data_list.append({
                    "Nama": input("Masukkan nama produk".ljust(35) + ": "),
                    "Harga": int(input("Masukkan harga produk".ljust(35) + ": ")),
                    "Jumlah": int(input("Masukkan jumlah produk".ljust(35) + ": "))
                })
            except ValueError:
                print("Harga yang anda masukkan tidak valid")
                continue

            while True:
                print("=" * 54)
                tambah = input("Tambah produk? (y/t)".ljust(35) + ": ").lower()
                print("=" * 54)

                if tambah in ("y", "t"):
                    break
                print("Input yang anda masukkan tidak valid")

            if tambah == "t":
                membuat_invoices(nama_kasir, data_list)
                break

    elif pilihan == "2":
        id_trx = input("Masukkan ID transaksi".ljust(35) + ": ")
        path = os.path.join(folder_invoices, id_trx + ".txt")

        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as f:
                print("=== ISI FILE ===")
                print(f.read())
        else:
            print(f"File '{id_trx}' tidak ditemukan.")

    elif pilihan == "3":
        print("Terima kasih!")
        break
    else:
        print("Opsi yang anda pilih tidak valid!")

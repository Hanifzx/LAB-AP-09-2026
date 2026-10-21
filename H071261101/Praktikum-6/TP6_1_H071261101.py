def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {"judul": judul, "penulis": penulis, "harga": harga, "stok": stok}
    inventaris.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan!")


def cari_buku(inventaris, kata_kunci):
    hasil = []
    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            hasil.append(buku)

    if len(hasil) == 0:
        print("Tidak ada buku yang cocok dengan kata kunci tersebut.")
    else:
        print(f"Ditemukan {len(hasil)} buku:")
        for i in range(len(hasil)):
            b = hasil[i] #mengambil buku ke-i dari hasil
            print(f" {i + 1}. {b['judul']} - {b['penulis']} | Rp{b['harga']} | Stok: {b['stok']}")


def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah
            if stok_baru < 0:
                print(f"Gagal! Stok '{buku['judul']}' tidak cukup (stok saat ini: {buku['stok']}).")
            else:
                buku["stok"] = stok_baru
                if jumlah > 0:
                    print(f"Stok '{buku['judul']}' bertambah {jumlah}. Stok sekarang: {stok_baru}")
                elif jumlah < 0:
                    print(f"Stok '{buku['judul']}' berkurang {abs(jumlah)}. Stok sekarang: {stok_baru}")
                else:
                    print(f"Stok '{buku['judul']}' tidak berubah. Stok sekarang: {stok_baru}")
            return 
    print(f"Error: buku '{judul}' tidak ditemukan!")


def ringkasan_inventaris(inventaris):
    print("=" * 40)
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("=" * 40)

    if len(inventaris) == 0:
        print("Inventaris masih kosong.")
        print("=" * 40)
        return

    total_stok = 0
    total_aset = 0
    termahal = inventaris[0]
    for buku in inventaris:
        total_stok += buku["stok"]
        total_aset += buku["harga"] * buku["stok"]
        if buku["harga"] > termahal["harga"]:
            termahal = buku

    print(f"Jumlah jenis buku : {len(inventaris)}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset : Rp{total_aset}")
    print(f"Buku termahal : {termahal['judul']} (Rp{termahal['harga']})")
    print("=" * 40)


def main():
    inventaris = []

    print("=" * 40)
    print("SISTEM INVENTARIS TOKO BUKU BOOKNEST")
    print("=" * 40)

    while True:
        print("Menu:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Update Stok")
        print("4. Ringkasan Inventaris")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            judul = input("Judul buku: ")
            penulis = input("Penulis: ")
            try:
                harga = int(input("Harga: "))
                stok = int(input("Stok awal: "))
                if harga < 0 or stok < 0:
                    print("Harga dan stok tidak boleh negatif!")
                else:
                    tambah_buku(inventaris, judul, penulis, harga, stok)
            except ValueError:
                print("Input tidak valid! Harga dan stok harus berupa angka.")

        elif pilihan == "2":
            kata_kunci = input("Masukkan kata kunci judul: ")
            cari_buku(inventaris, kata_kunci)

        elif pilihan == "3":
            judul = input("Judul buku yang ingin diupdate: ")
            try:
                jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
                update_stok(inventaris, judul, jumlah)
            except ValueError:
                print("Input tidak valid! Jumlah harus berupa angka.")

        elif pilihan == "4":
            ringkasan_inventaris(inventaris)

        elif pilihan == "5":
            print("Terima kasih telah menggunakan BookNest!")
            break

        else:
            print("Pilihan tidak valid! Masukkan angka 1-5.")


main()
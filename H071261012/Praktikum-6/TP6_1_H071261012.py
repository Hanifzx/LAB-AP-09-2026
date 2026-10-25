inventaris = []

def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    }
    inventaris.append(buku)
    print("Buku '" + judul + "' berhasil ditambahkan!")

def cari_buku(inventaris, kata_kunci):
    hasil = []
    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            hasil.append(buku)
    return hasil

def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah
            if stok_baru < 0:
                print("Gagal! Stok tidak boleh menjadi negatif.")
            else:
                buku["stok"] = stok_baru
                if jumlah >= 0:
                    print("Stok '" + buku["judul"] + "' bertambah " + str(jumlah) + ". Stok sekarang: " + str(stok_baru))
                else:
                    print("Stok '" + buku["judul"] + "' berkurang " + str(-jumlah) + ". Stok sekarang: " + str(stok_baru))
            return
    print("Error! Buku '" + judul + "' tidak ditemukan.")

def ringkasan_inventaris(inventaris):
    jumlah_jenis = len(inventaris)
    total_stok = 0
    total_aset = 0
    termahal = None

    for buku in inventaris:
        total_stok = total_stok + buku["stok"]
        total_aset = total_aset + buku["harga"] * buku["stok"]
        if termahal is None or buku["harga"] > termahal["harga"]:
            termahal = buku

    print("========================================")
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("========================================")
    print("Jumlah jenis buku :", jumlah_jenis)
    print("Total seluruh stok:", total_stok)
    print("Total nilai aset  : Rp" + str(total_aset))
    if termahal is None:
        print("Buku termahal     : -")
    else:
        print("Buku termahal     : " + termahal["judul"] + " (Rp" + str(termahal["harga"]) + ")")
    print("========================================")

print("========================================")
print(" SISTEM INVENTARIS TOKO BUKU BOOKNEST")
print("========================================")

while True:
    print("\nMenu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        judul = input("Judul buku: ")
        penulis = input("Penulis: ")
        try: #angka only bukan huruf
            harga = int(input("Harga: "))
            stok = int(input("Stok awal: "))
            if harga < 0 or stok < 0:
                print("Harga dan stok tidak boleh negatif!")
            else:
                tambah_buku(inventaris, judul, penulis, harga, stok)
        except ValueError:
            print("Input harga dan stok harus berupa angka!")

    elif pilihan == "2":
        kata_kunci = input("Masukkan kata kunci judul: ")
        hasil = cari_buku(inventaris, kata_kunci)
        if len(hasil) == 0:
            print("Tidak ada buku yang cocok.")
        else:
            print("Ditemukan " + str(len(hasil)) + " buku:")
            nomor = 1
            for buku in hasil:
                print(" " + str(nomor) + ". " + buku["judul"] + " - " + buku["penulis"] + " | Rp" + str(buku["harga"]) + " | Stok: " + str(buku["stok"]))
                nomor = nomor + 1

    elif pilihan == "3":
        judul = input("Judul buku yang ingin diupdate: ")
        try:
            jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
            update_stok(inventaris, judul, jumlah)
        except ValueError:
            print("Jumlah perubahan harus berupa angka!")

    elif pilihan == "4":
        ringkasan_inventaris(inventaris)

    elif pilihan == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break

    else:
        print("Pilihan tidak valid, masukkan angka 1-5.")
inventaris_toko = []

def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok,
    }
    inventaris.append(buku)
    print()
    print(f"Buku '{judul}' berhasil ditambahkan!")
    print()

def cari_buku(inventaris, kata_kunci):
    hasil = []
    for buku in inventaris:
        if kata_kunci in buku["judul"]:
            hasil.append(buku)
    urutan = 0
    panjang = len(hasil)
    print(f"Ditemukan {panjang} buku:")
    for hasil_nya in hasil:
        urutan += 1
        print(f"  {urutan}. {hasil_nya["judul"]} - {hasil_nya["penulis"]} | RP{hasil_nya["harga"]} | Stik: {hasil_nya["stok"]}")

def update_stok(inventaris, judul, jumlah):
    simbol = jumlah[0]
    angka = jumlah[1:]
    ditemukan = False
    for buku in inventaris:
        if buku["judul"] == judul:
            if simbol == "-":
                buku["stok"] -= int(angka)
                if buku["stok"] < 0:
                    print("Tidak dapat membuat perubahan")
                    buku["stok"] += int(angka)
                    ditemukan = True
                else:
                    print(f"Stok '{buku["judul"]}' berkurang {angka}. Stok sekarang: {buku["stok"]}")
                    ditemukan = True
            elif simbol == "+":
                buku["stok"] += int(angka)
                print(f"Stok '{buku["judul"]}' bertambah {angka}. Stok sekarang: {buku["stok"]}")
                ditemukan = True
    if not ditemukan:
        print(f"Tidak ada buku '{judul}' dalam inventaris")

def ringkasan_inventaris(inventaris):
    total_buku = len(inventaris)
    total_seluruh_stok = 0
    total_nilai_aset = 0
    buku_tertinggi = None
    harga_tertinggi = -1
    for i in inventaris:
        total_seluruh_stok += i["stok"]
        total_nilai_aset += i["harga"] * i["stok"]
        if i["harga"] > harga_tertinggi:
            buku_tertinggi = i["judul"]
            harga_tertinggi = i["harga"]
    print()
    print("===================================")
    print("  RINGKASAN INVENTARIS BOOKNEST")
    print("===================================")
    print(f"Jumlah jenis buku : {total_buku}")
    print(f"Total seluruh stok: {total_seluruh_stok}")
    print(f"Total nilai aset  : Rp{total_nilai_aset}")
    print(f"Buku termahal     : {buku_tertinggi} (Rp{harga_tertinggi})")
    print("===================================")

print()
print("=======================================")
print("  SISTEM IVENTARIS TOKO BUKU BOOKNEST")
print("=======================================")
while True:
    try:
        print()
        print("Menu:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Update Stok")
        print("4. Ringkasan Inventaris")
        print("5. Keluar")
        menu = int(input("Pilih menu (1-5): "))
        if menu == 1:
            judul_buku = input("Judul buku: ").title ()
            penulis = input("Penulis: ").title ()
            harga = int(input("Harga: "))
            stok = int(input("Stok awal: "))
            if harga < 0 or stok < 0:
                print("Harga atau stok tidak boleh mines")
                continue
            tambah_buku(inventaris_toko, judul_buku, penulis, harga, stok)
        elif menu == 2:
            mencari_buku = input("Masukkan kata kunci judul: ").title ()
            cari_buku(inventaris_toko, mencari_buku)
        elif menu == 3:
            judul_buku = input("Judul buku yang ingin diupdate: ").title ()
            jumlah_perubahan = input("Jumlah perubahan (positif=tambah, negatif=kurang): ")
            update_stok(inventaris_toko, judul_buku, jumlah_perubahan)
        elif menu == 4:
            ringkasan_inventaris(inventaris_toko)
        elif menu == 5:
            print("Terima kasih telah menggunakan BookNest!")
            break
        else:
            print("Input yang anda masukkan tidak valid")
    except:
        print("Input yang anda masukkan tidak valid")
        continue

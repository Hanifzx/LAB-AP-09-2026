#Soal 1: Sistem Inventaris Toko Buku "BookNest" 
def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {"Judul": judul, "Penulis": penulis, "Harga": harga, "Stok": stok}
    inventaris.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan!")
    print()

def cari_buku(inventaris, kata_kunci):
    hasil = []
    for buku in inventaris:
        if kata_kunci.lower() in buku["Judul"].lower():
            hasil.append(buku)

    if len(hasil) == 0:
        print("Buku tidak ditemukan.")
    else:
        print(f"Ditemukan {len(hasil)} buku")
        nomor = 1
        for buku in hasil:
            print(f" {nomor}. {buku['Judul']} - {buku['Penulis']} | Rp{buku['Harga']} | Stok: {buku['Stok']}")
            nomor += 1

def update_stok(inventaris, judul, jumlah):
    ketemu = False
    for buku in inventaris:
        if buku["Judul"].lower() == judul.lower():
            ketemu = True
            stok_baru = buku["Stok"] + jumlah
            if stok_baru < 0:
                print("Gagal! Stok tidak boleh menjadi negatif. ")
            else:
                buku["Stok"] = stok_baru
                if jumlah>= 0:
                    print(f"Stok '{buku['Judul']}' Bertambah {jumlah}. Stok sekarang: {stok_baru}")
                else:
                    print(f"Stok '{buku['Judul']}' Berkurang {abs(jumlah)}. Stok sekarang: {stok_baru}")

    if ketemu == False:
        print("Error: Buku tidak ditemukan!")

def ringkasan_inventaris(inventaris):
    print("========================================")
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("========================================")

    if len(inventaris) == 0:
        print("Inventaris masih kosong.")
    else:
        total_stok = 0
        total_aset = 0
        termahal = inventaris[0]
        
        for buku in inventaris:
            total_stok += buku["Stok"]
            total_aset += buku["Harga"] * buku["Stok"]
            if buku ["Harga"] > termahal["Harga"]:
                termahal = buku

        print(f"Jumlah jenis buku : {len(inventaris)}")
        print(f"Total seluruh stok: {total_stok}")
        print(f"Total nilai aset : Rp{total_aset}")
        print(f"Buku termahal : {termahal['Judul']} (Rp{termahal['Harga']})")
    print("========================================")


#PROGRAM UTAMA
inventaris = []

print("========================================")
print(" SISTEM INVENTARIS TOKO BUKU BOOKNEST")
print("========================================")

while True:
    print()
    print("Menu: ")
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
            print("Harga dan stok harus berupa angka!")

    elif pilihan == "2":
        kata_kunci = input("Masukkan kata kunci judul: ")
        cari_buku(inventaris, kata_kunci)

    elif pilihan == "3":
        judul = input("Judul buku yang ingin diupdate: ")
        try:
            jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
            update_stok(inventaris, judul, jumlah)
        except ValueError:
            print("Jumlah harus berupa angka!")

    elif pilihan == "4":
        ringkasan_inventaris(inventaris)

    elif pilihan == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break
    else:
        print("Pilihan tidak valid, pilih 1-5")
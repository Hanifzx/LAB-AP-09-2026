def format_durasi(detik):
    menit = detik // 60
    sisa = detik % 60
    return str(menit) + ":" + str(sisa)

def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)   # data lagu disimpan sebagai tuple
    playlist.append(lagu)
    genre_set.add(genre)
    print("Lagu '" + judul + "' oleh " + artis + " berhasil ditambahkan!")

def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return

    print("=======================================================")
    print("No  Judul                 Artis            Genre    Durasi")
    print("=======================================================")
    total = 0 # total durasi dalam detik
    nomor = 1 #no urut
    for lagu in playlist:
        print(str(nomor).ljust(4) + lagu[0].ljust(22) + lagu[1].ljust(17) + lagu[2].ljust(9) + format_durasi(lagu[3]))
        total = total + lagu[3] #tambah durasi lagu ke total
        nomor = nomor + 1
    print("=======================================================")
    print("Total durasi playlist: " + str(total // 60) + " menit " + str(total % 60) + " detik")

def filter_genre(playlist, genre_target):
    hasil = [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]
    return hasil

def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist): #periksa apakah sesuai jangkauan
        print("Nomor lagu tidak valid!")
    else:
        lagu = playlist.pop(nomor - 1)
        print("Lagu '" + lagu[0] + "' berhasil dihapus!")

def statistik_playlist(playlist, genre_set):
    print("========================================")
    print(" STATISTIK PLAYLIST PLAYTUNE")
    print("========================================")
    print(" Total lagu   :", len(playlist))
    print(" Jumlah genre :", len(genre_set))
    print(" Daftar genre :", genre_set)

    # hitung jumlah lagu per genre pakai dictionary
    hitungan = {}
    for lagu in playlist:
        genre = lagu[2]
        if genre in hitungan:
            hitungan[genre] = hitungan[genre] + 1
        else:
            hitungan[genre] = 1 #kategori baru dgn nilai 1

    print(" Distribusi genre:")
    for genre in hitungan:
        print("   " + genre + " : " + "#" * hitungan[genre] + " (" + str(hitungan[genre]) + ")")

    # cari lagu terpanjang dan terpendek
    if len(playlist) > 0:
        terpanjang = playlist[0]
        terpendek = playlist[0]
        for lagu in playlist:
            if lagu[3] > terpanjang[3]:
                terpanjang = lagu
            if lagu[3] < terpendek[3]:
                terpendek = lagu
        print(" Lagu terpanjang : " + terpanjang[0] + " (" + format_durasi(terpanjang[3]) + ")")
        print(" Lagu terpendek  : " + terpendek[0] + " (" + format_durasi(terpendek[3]) + ")")
    print("========================================")

# ---------- Program utama ----------
playlist = [] 
genre_set = set()

print("========================================")
print(" PLAYLIST MUSIK - PLAYTUNE")
print("========================================")

while True:
    print("\nMenu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")
    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        judul = input("Judul lagu: ")
        artis = input("Artis: ")
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip()
        try:
            durasi = int(input("Durasi (dalam detik): "))
            if durasi <= 0:
                print("Durasi harus angka positif!")
            else:
                tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
        except ValueError:
            print("Durasi harus berupa angka!")

    elif pilihan == "2":
        tampilkan_playlist(playlist)

    elif pilihan == "3":
        print("Genre tersedia:", genre_set)
        genre_target = input("Masukkan genre yang ingin difilter: ")
        hasil = filter_genre(playlist, genre_target)
        if len(hasil) == 0:
            print("Tidak ada lagu bergenre '" + genre_target + "'.")
        else:
            print("Lagu bergenre '" + genre_target + "':")
            nomor = 1
            for lagu in hasil:
                print(" " + str(nomor) + ". " + lagu[0] + " - " + lagu[1] + " (" + format_durasi(lagu[3]) + ")")
                nomor = nomor + 1

    elif pilihan == "4":
        if len(playlist) == 0:
            print("Playlist masih kosong.")
        else:
            tampilkan_playlist(playlist)
            try:
                nomor = int(input("Nomor lagu yang ingin dihapus: "))
                hapus_lagu(playlist, nomor)
            except ValueError:
                print("Nomor harus berupa angka!")

    elif pilihan == "5":
        statistik_playlist(playlist, genre_set)

    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan tidak valid, masukkan angka 1-6.")
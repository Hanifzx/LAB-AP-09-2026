def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre)

    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!\n")


def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("Playlist masih kosong!")
        return

    print("=" * 75)
    print(f"{'No':<5}{'Judul':<25}{'Artis':<20}{'Genre':<12}{'Durasi'}")
    print("=" * 75)

    total_durasi = 0

    for i, lagu in enumerate(playlist, start=1):
        judul, artis, genre, durasi = lagu

        menit = durasi // 60
        detik = durasi % 60

        print(f"{i:<5}{judul:<25}{artis:<20}{genre:<12}{menit}:{detik:02d}")

        total_durasi += durasi

    total_menit = total_durasi // 60
    sisa_detik = total_durasi % 60

    print("=" * 75)
    print(f"Total durasi playlist: {total_menit} menit {sisa_detik} detik")


def filter_genre(playlist, genre_target):
    hasil_filter = [
        lagu for lagu in playlist
        if lagu[2].lower() == genre_target.lower()
    ]

    return hasil_filter


def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        print("Nomor lagu tidak valid!")
        return

    lagu = playlist.pop(nomor - 1)
    print(f"Lagu '{lagu[0]}' berhasil dihapus!")


def statistik_playlist(playlist, genre_set):
    print("=" * 45)
    print("STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 45)

    print(f"Total lagu   : {len(playlist)}")
    print(f"Jumlah genre : {len(genre_set)}")
    print(f"Daftar genre : {genre_set}")

    if len(playlist) == 0:
        print("Belum ada lagu untuk dihitung.")
        print("=" * 45)
        return

    distribusi = {}

    for lagu in playlist:
        genre = lagu[2]

        if genre in distribusi:
            distribusi[genre] += 1
        else:
            distribusi[genre] = 1

    print("Distribusi genre:")

    for genre, jumlah in distribusi.items():
        print(f"  {genre:<12}: ({jumlah})")

    lagu_terpanjang = max(playlist, key=lambda lagu: lagu[3])
    lagu_terpendek = min(playlist, key=lambda lagu: lagu[3])

    durasi_panjang = lagu_terpanjang[3]
    durasi_pendek = lagu_terpendek[3]

    print(
        f"Lagu terpanjang: {lagu_terpanjang[0]} "
        f"({durasi_panjang // 60}:{durasi_panjang % 60:02d})"
    )

    print(
        f"Lagu terpendek : {lagu_terpendek[0]} "
        f"({durasi_pendek // 60}:{durasi_pendek % 60:02d})"
    )

    print("=" * 45)

playlist = []
genre_set = set()

print("=" * 45)
print("PLAYLIST MUSIK - PLAYTUNE")
print("=" * 45)

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
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").title()

        try:
            durasi = int(input("Durasi (dalam detik): "))

            if durasi <= 0:
                print("Durasi harus berupa angka positif!")
            elif judul == "" or artis == "" or genre == "":
                print("Judul, artis, dan genre tidak boleh kosong!")
            else:
                tambah_lagu(
                    playlist, genre_set,
                    judul, artis, genre, durasi
                )

        except ValueError:
            print("Durasi harus berupa angka!")

    elif pilihan == "2":
        tampilkan_playlist(playlist)

    elif pilihan == "3":
        if len(genre_set) == 0:
            print("Belum ada genre karena playlist masih kosong!")
        else:
            print("Genre tersedia:", genre_set)
            genre_target = input(
                "Masukkan genre yang ingin difilter: "
            )

            hasil = filter_genre(playlist, genre_target)

            if len(hasil) == 0:
                print(f"Tidak ada lagu bergenre '{genre_target}'.")
            else:
                print(f"Lagu bergenre '{genre_target}':")

                for i, lagu in enumerate(hasil, start=1):
                    judul, artis, genre, durasi = lagu
                    menit = durasi // 60
                    detik = durasi % 60

                    print(
                        f"  {i}. {judul} - {artis} "
                        f"({menit}:{detik:02d})"
                    )

    elif pilihan == "4":
        if len(playlist) == 0:
            print("Playlist masih kosong!")
        else:
            tampilkan_playlist(playlist)

            try:
                nomor = int(input("Nomor lagu yang ingin dihapus: "))
                hapus_lagu(playlist, nomor)

                genre_set = {lagu[2] for lagu in playlist}

            except ValueError:
                print("Nomor lagu harus berupa angka!")

    elif pilihan == "5":
        statistik_playlist(playlist, genre_set)

    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan tidak valid! Silakan pilih menu 1-6.")

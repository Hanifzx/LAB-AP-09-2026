def format_durasi(detik):
    menit, sisa = divmod(detik, 60)
    return f"{menit}:{sisa:02d}"


def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    genre = genre.strip().capitalize()
    lagu = (judul, artis, genre, durasi)  # tuple: data lagu tidak diubah lagi
    playlist.append(lagu)
    genre_set.add(genre)  # set otomatis mencegah genre ganda
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")


def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return

    print("=" * 55)
    print(f"{'No':<4}{'Judul':<22}{'Artis':<16}{'Genre':<8}{'Durasi':>5}")
    print("=" * 55)
    total = 0
    for i in range(len(playlist)):
        judul, artis, genre, durasi = playlist[i]  # tuple unpacking
        print(f"{i + 1:<4}{judul:<22}{artis:<16}{genre:<8}{format_durasi(durasi):>5}")
        total += durasi
    print("=" * 55)
    print(f"Total durasi playlist: {total // 60} menit {total % 60} detik")


def filter_genre(playlist, genre_target):
    # list comprehension: ambil lagu yang genre-nya (indeks 2) sama dengan target
    return [lagu for lagu in playlist if lagu[2].lower() == genre_target.strip().lower()]


def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        print("Nomor lagu tidak valid!")
        return False
    lagu = playlist.pop(nomor - 1)  # nomor tampilan mulai 1, indeks list mulai 0
    print(f"Lagu '{lagu[0]}' berhasil dihapus!")
    return True


def statistik_playlist(playlist, genre_set):
    print("=" * 40)
    print(" STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 40)

    if len(playlist) == 0:
        print(" Playlist masih kosong.")
        print("=" * 40)
        return

    # dictionary untuk menghitung jumlah lagu per genre
    hitungan = {}
    for lagu in playlist:
        hitungan[lagu[2]] = hitungan.get(lagu[2], 0) + 1

    terpanjang = playlist[0]
    terpendek = playlist[0]
    for lagu in playlist:
        if lagu[3] > terpanjang[3]:
            terpanjang = lagu
        if lagu[3] < terpendek[3]:
            terpendek = lagu

    print(f" Total lagu : {len(playlist)}")
    print(f" Jumlah genre : {len(genre_set)}")
    print(f" Daftar genre : {genre_set}")
    print(" Distribusi genre:")
    for genre in hitungan:
        print(f" {genre} : {'#' * hitungan[genre]} ({hitungan[genre]})")
    print(f" Lagu terpanjang : {terpanjang[0]} ({format_durasi(terpanjang[3])})")
    print(f" Lagu terpendek : {terpendek[0]} ({format_durasi(terpendek[3])})")
    print("=" * 40)


def main():
    playlist = []
    genre_set = set()

    print("=" * 40)
    print(" PLAYLIST MUSIK - PLAYTUNE")
    print("=" * 40)

    while True:
        print("Menu:")
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
            genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ")
            try:
                durasi = int(input("Durasi (dalam detik): "))
                if durasi <= 0:
                    print("Durasi harus berupa angka positif!")
                else:
                    tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
            except ValueError:
                print("Input tidak valid! Durasi harus berupa angka.")

        elif pilihan == "2":
            tampilkan_playlist(playlist)

        elif pilihan == "3":
            if len(playlist) == 0:
                print("Playlist masih kosong.")
            else:
                print(f"Genre tersedia: {genre_set}")
                target = input("Masukkan genre yang ingin difilter: ")
                hasil = filter_genre(playlist, target)
                if len(hasil) == 0:
                    print(f"Tidak ada lagu bergenre '{target}'.")
                else:
                    print(f"Lagu bergenre '{target.strip().capitalize()}':")
                    for i in range(len(hasil)):
                        print(f" {i + 1}. {hasil[i][0]} - {hasil[i][1]} ({format_durasi(hasil[i][3])})")

        elif pilihan == "4":
            if len(playlist) == 0:
                print("Playlist masih kosong.")
            else:
                tampilkan_playlist(playlist)
                try:
                    nomor = int(input("Nomor lagu yang ingin dihapus: "))
                    if hapus_lagu(playlist, nomor):
                        genre_set.clear()
                        for lagu in playlist:
                            genre_set.add(lagu[2])
                except ValueError:
                    print("Input tidak valid! Nomor harus berupa angka.")

        elif pilihan == "5":
            statistik_playlist(playlist, genre_set)

        elif pilihan == "6":
            print("Terima kasih telah menggunakan PlayTune!")
            break

        else:
            print("Pilihan tidak valid! Masukkan angka 1-6.")


main()
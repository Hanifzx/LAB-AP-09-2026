#Soal 3: Sistem Manajemen Playlist Musik "PlayTune"
def format_durasi(detik):
    menit = detik // 60
    sisa = detik % 60
    return f"{menit}:{sisa:02d}"


def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")


def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
    else:
        print("=" * 55)
        print(f"{'No':<4}{'Judul':<24}{'Artis':<16}{'Genre':<8}Durasi")
        print("=" * 55)
        nomor = 1
        total_detik = 0
        for lagu in playlist:
            print(f"{nomor:<4}{lagu[0]:<24}{lagu[1]:<16}{lagu[2]:<8}{format_durasi(lagu[3])}")
            total_detik += lagu[3]
            nomor += 1
        print("=" * 55)
        print(f"Total durasi playlist: {total_detik // 60} menit {total_detik % 60} detik")


def filter_genre(playlist, genre_target):
    hasil = [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]
    return hasil


def hapus_lagu(playlist, nomor):
    if nomor >= 1 and nomor <= len(playlist):
        lagu = playlist.pop(nomor - 1)
        print(f"Lagu '{lagu[0]}' berhasil dihapus!")
    else:
        print("Nomor lagu tidak valid!")


def statistik_playlist(playlist, genre_set):
    print("========================================")
    print(" STATISTIK PLAYLIST PLAYTUNE")
    print("========================================")

    if len(playlist) == 0:
        print(" Playlist masih kosong.")
    else:
        distribusi = {}
        terpanjang = playlist[0]
        terpendek = playlist[0]
        for lagu in playlist:
            genre = lagu[2]
            if genre in distribusi:
                distribusi[genre] += 1
            else:
                distribusi[genre] = 1

            if lagu[3] > terpanjang[3]:
                terpanjang = lagu
            if lagu[3] < terpendek[3]:
                terpendek = lagu

        print(f" Total lagu : {len(playlist)}")
        print(f" Jumlah genre : {len(genre_set)}")
        print(f" Daftar genre : {genre_set}")
        print(" Distribusi genre:")
        for genre in distribusi:
            jumlah = distribusi[genre]
            print(f" {genre} : # ({jumlah})")
        print(f" Lagu terpanjang : {terpanjang[0]} ({format_durasi(terpanjang[3])})")
        print(f" Lagu terpendek : {terpendek[0]} ({format_durasi(terpendek[3])})")
    print("========================================")


# ===== PROGRAM UTAMA =====
playlist = []
genre_set = set()
genre_valid = ["Pop", "Rock", "Jazz", "RnB", "Dangdut"]

print("========================================")
print(" PLAYLIST MUSIK - PLAYTUNE")
print("========================================")

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
        genre_input = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip()

        genre = ""
        for g in genre_valid:
            if g.lower() == genre_input.lower():
                genre = g

        if genre == "":
            print("Genre tidak valid! Pilih salah satu: Pop/Rock/Jazz/RnB/Dangdut")
        else:
            try:
                durasi = int(input("Durasi (dalam detik): "))
                if durasi <= 0:
                    print("Durasi harus lebih dari 0!")
                else:
                    tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
            except ValueError:
                print("Durasi harus berupa angka!")

    elif pilihan == "2":
        tampilkan_playlist(playlist)

    elif pilihan == "3":
        print(f"Genre tersedia: {genre_set}")
        target = input("Masukkan genre yang ingin difilter: ").strip()
        hasil = filter_genre(playlist, target)
        if len(hasil) == 0:
            print(f"Tidak ada lagu bergenre '{target}'.")
        else:
            print(f"Lagu bergenre '{target}':")
            nomor = 1
            for lagu in hasil:
                print(f" {nomor}. {lagu[0]} - {lagu[1]} ({format_durasi(lagu[3])})")
                nomor += 1

    elif pilihan == "4":
        if len(playlist) == 0:
            print("Playlist masih kosong.")
        else:
            tampilkan_playlist(playlist)
            try:
                nomor = int(input("Nomor lagu yang ingin dihapus: "))
                hapus_lagu(playlist, nomor)
                # perbarui genre_set sesuai lagu yang masih ada
                genre_set.clear()
                for lagu in playlist:
                    genre_set.add(lagu[2])
            except ValueError:
                print("Nomor harus berupa angka!")

    elif pilihan == "5":
        statistik_playlist(playlist, genre_set)

    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan tidak valid, pilih 1-6.")


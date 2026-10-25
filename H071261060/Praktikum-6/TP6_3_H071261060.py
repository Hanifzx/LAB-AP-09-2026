playlist_nya = []
genre_unik = set()
genre = ["Pop", "Rock", "Jazz", "RnB", "Dangdut"]

def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = {
        "judul": judul,
        "artis": artis,
        "genre": genre,
        "durasi": durasi,
    }
    playlist.append(lagu)
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")
    print()

def  tampilkan_playlist(playlist):
    total_durasi = 0
    lagu_terpanjang = 0
    artis_terpanjang = 0
    genre_terpanjang = 0
    durasi_terpanjang = 0
    for lagu in playlist:
        total_durasi += lagu["durasi"]
        lagu_panjang = lagu["judul"]
        artis = lagu["artis"]
        genre = lagu["genre"]
        durasi = lagu["durasi"]
        if len(lagu_panjang) > lagu_terpanjang:
            lagu_terpanjang = len(lagu_panjang)
        if len(artis) > artis_terpanjang:
            artis_terpanjang = len(artis)
        if len(genre) > genre_terpanjang:
            genre_terpanjang = len(genre)
        if len(str(durasi)) > durasi_terpanjang:
            durasi_terpanjang = len(str(durasi))
    print(f"====={lagu_terpanjang * "=" }=={artis_terpanjang * "=" }=={genre_terpanjang * "=" }==={durasi_terpanjang * "=" }===")
    print(f" No  Judul{(lagu_terpanjang - 5) * " "}  Artis{(artis_terpanjang - 5) * " "}  Genre{(genre_terpanjang - 5) * " "}  Durasi")
    print(f"====={lagu_terpanjang * "=" }=={artis_terpanjang * "=" }=={genre_terpanjang * "=" }==={durasi_terpanjang * "=" }===")
    baris_ke = 1
    for i in playlist:
        untuk_genre = i["genre"]
        menit = i["durasi"] // 60
        detik = i["durasi"] % 60
        print(f" {baris_ke}   {i["judul"].ljust(lagu_terpanjang)}  {i["artis"].ljust(artis_terpanjang)}  {i["genre"].ljust(genre_terpanjang)}   {menit}:{detik}")
        baris_ke += 1
    print(f"====={lagu_terpanjang * "=" }=={artis_terpanjang * "=" }=={genre_terpanjang * "=" }==={durasi_terpanjang * "=" }===")
    print(f"Total durasi playlist: {total_durasi // 60} menit {total_durasi % 60} detik")
    print()

def filter_genre(playlist, genre_target):
    urutan = 1
    print(f"Lagu bergenre '{genre_target}':")
    for lagu in playlist:
        if lagu["genre"] == genre_target:
            lagu_nya = lagu["judul"]
            artis = lagu["artis"]
            durasi = lagu["durasi"]
            print(f"  {urutan}. {lagu_nya} - {artis} ({durasi // 60}:{durasi % 60})")
            urutan += 1
        elif genre_target not in lagu["genre"]:
            print("Tidak ada genre")

def hapus_lagu(playlist, nomor):
    playlist.pop(nomor-1)
    genre_unik.clear()
    for lagu in playlist: 
        genre_unik.add(lagu["genre"])
    print(f"Lagu nomor {nomor} telah berhasil dihapus!")
    tampilkan_playlist(playlist)

def statistik_playlist(playlist, genre_set):
    distribusi_genre = {}
    lagu_terpanjang = None
    waktu_terpanjang = -1
    lagu_terpendek = -1
    waktu_terpendek = None
    for lagu in playlist:
        if lagu["durasi"] > waktu_terpanjang:
            lagu_terpanjang = lagu["judul"]
            waktu_terpanjang = lagu["durasi"]
        else:
            lagu_terpendek = lagu["judul"]
            waktu_terpendek = lagu["durasi"]
    if lagu_terpendek == -1 and waktu_terpendek == None:
        lagu_terpendek = lagu_terpanjang
        waktu_terpendek = waktu_terpanjang
    print("===============================================")
    print("       STATISTIK PLAYLIST PLAYTUNE")
    print("===============================================")
    print(f"Total lagu        : {len(playlist)}")
    print(f"Jumlah genre      : {len(genre_set)}")
    print(f"Daftar genre      : {genre_set}")
    print()
    print("Distribusi genre: ")
    for lagu in playlist:
        genre = lagu["genre"]
        if genre in distribusi_genre:
            distribusi_genre[genre] += 1
        else:
            distribusi_genre[genre] = 1
    for genre, jumlah in distribusi_genre.items():
        print(f"  {genre}        : # ({jumlah})")
    print()
    print(f"Lagu terpanjang : {lagu_terpanjang} ({waktu_terpanjang // 60}:{waktu_terpanjang % 60})")
    print(f"Lagu terpendek  : {lagu_terpanjang} ({waktu_terpendek // 60}:{waktu_terpendek % 60})")
    print("===============================================")

def list(playlist):
    return playlist

print("===============================")
print("   PLAYLIST MUSIK - PLAYTUNE")
print("===============================")
print("Menu:")
print("1. Tambah Lagu")
print("2. Tampilkan Playlist")
print("3. Filter berdasarkan Genre")
print("4. Hapus Lagu")
print("5. Statistik Playlist")
print("6. Keluar")
while True:
    try:
        menu = int(input("Pilih menu (1-6): "))
    except:
        print("Input yang anda masukkan tidak valid")
        continue
    try:
        if menu == 1:
            judul_lagu = input("Judul lagu: ").title ()
            artis_lagu = input("Artis: ").title ()
            genre_lagu = input("(Pop/Rock/Jazz/RnB/Dangdut): ")
            if genre_lagu not in genre:
                print("Genre yang anda masukkan tidak valid")
                continue
            durasi_lagu = int(input("Durasi (dalam detik): "))
            tambah_lagu(playlist_nya, genre_unik, judul_lagu, artis_lagu, genre_lagu, durasi_lagu)
        elif menu == 2:
            print()
            tampilkan_playlist(playlist_nya)
        elif menu == 3:
            if not genre_unik:
                print("Masukkan lagu terlebih dahulu")
                print()
                continue
            print(f"Genre tersedia: {genre_unik}")
            filter_genrenya = input("Masukkan genre yang ingin difilter: ")
            filter_genre(playlist_nya, filter_genrenya)
        elif menu == 4:
            tampilkan_playlist(playlist_nya)
            nomor  = int(input("Masukkan nomor lagu yang ingin di hapus: "))
            hapus_lagu(playlist_nya, nomor)
        elif menu == 5:
            statistik_playlist(playlist_nya, genre_unik)
        elif menu == 6:
            print("Terima kasih telah menggunakan PlayTune!")
            break
    except:
        print("Input yang anda masukkan tidak valid")
        continue
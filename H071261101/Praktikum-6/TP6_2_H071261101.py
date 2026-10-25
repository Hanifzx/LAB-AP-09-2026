def daftar_kandidat(kandidat_set, nama):
    nama = nama.capitalize()
    if nama in kandidat_set:
        print(f"'{nama}' sudah terdaftar sebelumnya!")
    else:
        kandidat_set.add(nama)
        print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pilihan = pilihan.capitalize()
    kunci_pemilih = nama_pemilih.lower()  
    if pilihan not in kandidat_set:
        print(f"Error: '{pilihan}' bukan kandidat. Suara tidak dicatat!")
    elif kunci_pemilih in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
    else:
        rekap_suara[kunci_pemilih] = pilihan
        print(f"Suara '{nama_pemilih}' untuk '{pilihan}' berhasil dicatat!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}
    for kandidat in kandidat_set:
        perolehan[kandidat] = 0  
    for pemilih in rekap_suara:
        perolehan[rekap_suara[pemilih]] += 1
    return perolehan


def tampilkan_hasil(perolehan):
    print("=" * 40)
    print(" HASIL PEMILIHAN KETUA KELAS")
    print("=" * 40)

    total = 0
    for kandidat in sorted(perolehan):
        print(f" {kandidat}: {perolehan[kandidat]} suara")
        total += perolehan[kandidat]
    print(f"Total suara masuk: {total}")

    if total == 0:
        print("Belum ada suara yang masuk, tidak ada pemenang.")
    else:
        suara_tertinggi = max(perolehan.values())
        pemenang = []
        for kandidat in sorted(perolehan):
            if perolehan[kandidat] == suara_tertinggi:
                pemenang.append(kandidat)

        if len(pemenang) == 1:
            print(f"PEMENANG: {pemenang[0]} dengan {suara_tertinggi} suara!")
        else:
            print(f"Hasil SERI antara: {', '.join(pemenang)}")
            print("Perlu dilakukan pemilihan ulang!")
    print("=" * 40)


def main():
    kandidat_set = set()
    rekap_suara = {}

    print("=" * 40)
    print(" SISTEM PEMILIHAN KETUA KELAS")
    print("=" * 40)

    print("--- FASE PENDAFTARAN KANDIDAT ---")
    while True:
        nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()
        if nama == "":
            if len(kandidat_set) < 2:
                print("Minimal harus ada 2 kandidat sebelum lanjut!")
            else:
                break
        else:
            daftar_kandidat(kandidat_set, nama)
    print(f"Kandidat terdaftar: {kandidat_set}")

    print("--- FASE PEMUNGUTAN SUARA ---")
    while True:
        nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ").strip()
        if nama_pemilih == "":
            break
        print(f"Kandidat yang tersedia: {kandidat_set}")
        pilihan = input("Pilih kandidat: ").strip()
        berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

    perolehan = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(perolehan)
main()
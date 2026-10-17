# Soal 2: Sistem Pemilihan Ketua Kelas "VoteClass" 
def daftar_kandidat(kandidat_set, nama):
    nama = nama.capitalize()
    if nama in kandidat_set:
        print(f"'{nama}' sudah terdaftar!")
    else:
        kandidat_set.add(nama)
        print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pemilih = nama_pemilih.lower()
    pilihan = pilihan.capitalize()

    if pilihan not in kandidat_set:
        print(f"Kandidat '{pilihan}' tidak ada! Suara tidak dicatat.")
    elif pemilih in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
    else:
        rekap_suara[pemilih] = pilihan
        print(f"Suara '{nama_pemilih}' untuk '{pilihan}' berhasil dicatat!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}
    for kandidat in kandidat_set:
        perolehan[kandidat] = 0

    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1

    return perolehan


def tampilkan_hasil(perolehan):
    print("========================================")
    print(" HASIL PEMILIHAN KETUA KELAS")
    print("========================================")

    total = 0
    for kandidat in sorted(perolehan):
        print(f" {kandidat}: {perolehan[kandidat]} suara")
        total += perolehan[kandidat]
    print(f"Total suara masuk: {total}")

    if total == 0:
        print("Belum ada suara yang masuk.")
    else:
        tertinggi = max(perolehan.values())
        pemenang = []
        for kandidat in sorted(perolehan):
            if perolehan[kandidat] == tertinggi:
                pemenang.append(kandidat)

        if len(pemenang) > 1:
            print("Hasil SERI antara: " + ", ".join(pemenang))
            print("Perlu dilakukan pemilihan ulang!")
        else:
            print(f"PEMENANG: {pemenang[0]} dengan {tertinggi} suara!")
    print("========================================")


#PROGRAM UTAMA
kandidat_set = set()
rekap_suara = {}

print("========================================")
print(" SISTEM PEMILIHAN KETUA KELAS")
print("========================================")
print()
print("--- FASE PENDAFTARAN KANDIDAT ---")
while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()
    if nama == "":
        if len(kandidat_set) < 2:
            print("Minimal harus ada 2 kandidat!")
        else:
            break
    else:
        daftar_kandidat(kandidat_set, nama)
print(f"Kandidat terdaftar: {kandidat_set}")
print()
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
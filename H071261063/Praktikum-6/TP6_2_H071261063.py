
def daftar_kandidat(kandidat_set, nama):
    nama = nama.capitalize()

    if nama in kandidat_set:
        print(f"'{nama}' sudah terdaftar!")
    else:
        kandidat_set.add(nama)
        print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pemilih_key = nama_pemilih.lower()
    pilihan = pilihan.capitalize()

    if pemilih_key in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
        return

    if pilihan not in kandidat_set:
        print(f"Error! Kandidat '{pilihan}' tidak terdaftar.")
        return

    rekap_suara[pemilih_key] = pilihan
    print(f"Suara '{nama_pemilih}' untuk '{pilihan}' berhasil dicatat!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}

    for nama in kandidat_set:
        perolehan[nama] = 0

    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1

    return perolehan


def tampilkan_hasil(perolehan):
    total_suara = sum(perolehan.values())
    suara_tertinggi = max(perolehan.values())
    pemenang = []

    print("=" * 40)
    print("  HASIL PEMILIHAN KETUA KELAS")
    print("=" * 40)

    for nama, jumlah in perolehan.items():
        print(f"  {nama}: {jumlah} suara")

    print(f"Total suara masuk: {total_suara}")

    for nama, jumlah in perolehan.items():
        if jumlah == suara_tertinggi:
            pemenang.append(nama)

    if total_suara == 0:
        print("Belum ada suara yang masuk.")
    elif len(pemenang) > 1:
        print("Hasil SERI antara: " + ", ".join(pemenang))
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print(f"PEMENANG: {pemenang[0]} dengan {suara_tertinggi} suara!")

    print("=" * 40)


kandidat_set = set()
rekap_suara = {}

print("=" * 40)
print("  SISTEM PEMILIHAN KETUA KELAS")
print("=" * 40)

print("--- FASE PENDAFTARAN KANDIDAT ---")

while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")

    if nama == "":
        break

    daftar_kandidat(kandidat_set, nama)

print("Kandidat terdaftar:", kandidat_set)

if len(kandidat_set) < 2:
    print("Error! Minimal harus ada 2 kandidat untuk melanjutkan.")
else:
    print("--- FASE PEMUNGUTAN SUARA ---")

    while True:
        nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ")

        if nama_pemilih == "":
            break

        print("Kandidat yang tersedia:", kandidat_set)
        pilihan = input("Pilih kandidat: ")

        berikan_suara(
            rekap_suara,
            kandidat_set,
            nama_pemilih,
            pilihan
        )

    perolehan = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(perolehan)

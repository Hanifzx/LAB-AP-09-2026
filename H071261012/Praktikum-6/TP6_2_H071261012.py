def daftar_kandidat(kandidat_set, nama):
    nama = nama.capitalize()
    if nama in kandidat_set:
        print("'" + nama + "' sudah terdaftar sebelumnya!")
    else:
        kandidat_set.add(nama)
        print("'" + nama + "' berhasil didaftarkan sebagai kandidat!")

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pilihan = pilihan.capitalize()
    kunci = nama_pemilih.lower()

    if kunci in rekap_suara:
        print("'" + nama_pemilih + "' sudah memberikan suara sebelumnya!")
    elif pilihan not in kandidat_set:
        print("Error! Kandidat '" + pilihan + "' tidak ada. Suara tidak dicatat.")
    else:
        rekap_suara[kunci] = pilihan #suara dicatat
        print("Suara '" + nama_pemilih + "' untuk '" + pilihan + "' berhasil dicatat!")

def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}
    for kandidat in kandidat_set:
        perolehan[kandidat] = 0 #yg tdk dipilih tetap 0
    for pemilih in rekap_suara:
        pilihan = rekap_suara[pemilih] #ambil nama kandidat yg dia pilih
        perolehan[pilihan] = perolehan[pilihan] + 1
    return perolehan

def tampilkan_hasil(perolehan):
    print("========================================")
    print(" HASIL PEMILIHAN KETUA KELAS")
    print("========================================")

    total = 0 #jumlah semua suara
    tertinggi = 0
    for kandidat in sorted(perolehan):
        suara = perolehan[kandidat]
        print(" " + kandidat + ": " + str(suara) + " suara")
        total = total + suara
        if suara > tertinggi:
            tertinggi = suara

    print("Total suara masuk:", total)
 
    # cari siapa saja yang punya suara tertinggi/seri
    pemenang = []
    for kandidat in sorted(perolehan):
        if perolehan[kandidat] == tertinggi:
            pemenang.append(kandidat)

    if total == 0: 
        print("Belum ada suara yang masuk.")
    elif len(pemenang) > 1:
        print("Hasil SERI antara: " + ", ".join(pemenang)) #gabung nama dgn ,
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print("PEMENANG: " + pemenang[0] + " dengan " + str(tertinggi) + " suara!")
    print("========================================")

print("========================================")
print(" SISTEM PEMILIHAN KETUA KELAS")
print("========================================")

print("\n--- FASE PENDAFTARAN KANDIDAT ---")
kandidat_set = set()

while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()
    if nama == "":
        if len(kandidat_set) < 2:
            print("Minimal harus ada 2 kandidat!")
        else:
            break
    else:
        daftar_kandidat(kandidat_set, nama)

print("\nKandidat terdaftar:", kandidat_set)

# Fase pemungutan suara
print("\n--- FASE PEMUNGUTAN SUARA ---")
rekap_suara = {}
while True:
    nama_pemilih = input("\nNama pemilih (kosongkan untuk selesai): ").strip()
    if nama_pemilih == "":
        break
    print("Kandidat yang tersedia:", kandidat_set)
    pilihan = input("Pilih kandidat: ").strip()
    berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

# Hasil
perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)
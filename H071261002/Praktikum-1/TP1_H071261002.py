kategori_usia_dan_keanggotaan = int(input("kategori_usia_17_dan_anggota:" ))

if kategori_usia < 5:
    print("gratis")
if kategori_usia >= 5 and kategori_usia <= 12:
    print("harga tiket Rp 50.000")
if kategori_usia >= 13 and kategori_usia <= 59:
    print("harga tiket Rp 100.000")
if kategori_usia > 60:
    print("harga tiket Rp 70.000")

else :
    anggota = diskon_20_percent
    hasil = "harga diskon" if anggota else "harga tanpa diskon"

if kategori_usia_dan_keanggotaan == 17 and anggota:
    print(hasil)
    
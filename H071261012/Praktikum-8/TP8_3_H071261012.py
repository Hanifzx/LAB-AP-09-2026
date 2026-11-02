import re

# menghapus spasi dan tanda - dari nomor
def bersihkan_nomor(nomor):
    hasil = re.sub(r"[ -]", "", nomor)
    return hasil

# cek apakah nomor (yg udh bersih) valid: 10 sampai 13 digit angka
def cek_nomor(nomor):
    pola = r"^\d{10,13}$"
    if re.match(pola, nomor):
        return True
    else:
        return False

print("=== Pembersihan Data Nomor Telepon ===")
print()

jumlah = int(input("Masukkan jumlah data: "))
print()

data_sebelum = []
data_sesudah = []
nomor_valid = []

# looping untuk menerima setiap nomor
for i in range(jumlah):
    nomor = input("Nomor ke-" + str(i + 1) + ": ")
    print()

    bersih = bersihkan_nomor(nomor)

    data_sebelum.append(nomor)
    data_sesudah.append(bersih)

    # hanya nomor yg valid dimasukkan ke list
    if cek_nomor(bersih):
        nomor_valid.append(bersih)

print("--- Hasil Pembersihan ---")
print()

#tampilkan data satu satu & statusnya
for i in range(jumlah):
    print("Data " + str(i + 1) + ":")
    print("Sebelum :", data_sebelum[i])
    print("Sesudah :", data_sesudah[i])

    if cek_nomor(data_sesudah[i]):
        print("Status  : Valid")
    else:
        print("Status  : Tidak valid")
    print()

print("Jumlah nomor valid:", len(nomor_valid))
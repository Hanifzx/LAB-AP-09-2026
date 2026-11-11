import re

def bersihkan(nomor):
    return re.sub(r"[\s-]", "", nomor)  # hapus spasi dan tanda -

def validasi_telp(nomor):
    return re.match(r"^\d{10,13}$", nomor) is not None

print("=== Pembersihan Data Nomor Telepon ===\n")
jumlah = int(input("Masukkan jumlah data: "))

data_sebelum = []
data_sesudah = []
status = []
nomor_valid = []

for i in range(1, jumlah + 1):
    nomor = input(f"\nNomor ke-{i}: ")
    bersih = bersihkan(nomor)

    data_sebelum.append(nomor)
    data_sesudah.append(bersih)

    if validasi_telp(bersih):
        status.append("Valid")
        nomor_valid.append(bersih)
    else:
        status.append("Tidak valid")

print("\n--- Hasil Pembersihan ---")
for i in range(jumlah):
    print(f"\nData {i + 1}:")
    print(f"Sebelum : {data_sebelum[i]}")
    print(f"Sesudah : {data_sesudah[i]}")
    print(f"Status  : {status[i]}")

print(f"\nJumlah nomor valid: {len(nomor_valid)}")
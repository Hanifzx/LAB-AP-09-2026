# CONDITIONAL STATEMENT II

print("--- Setup Denah Bioskop NontonYuk ---")

while True:
    try:
        N = int(input("Masukkan jumlah baris: "))

        if N <= 0:
            print("Jumlah baris harus lebih dari 0!")
            continue

        break

    except:
        print("Input baris harus berupa angka!")

while True:
    try:
        M = int(input("Masukkan jumlah kursi: "))

        if M <= 0:
            print("Jumlah baris harus lebih dari 0!")
            continue

        break

    except:
        print("Input baris harus berupa angka!")

print()
print("--- Daftar Kursi Tersedia ---")

for baris in range(1, N + 1):
    for kursi in range(1, M + 1):
        if kursi == 13: continue
        if baris == 1 and kursi % 2 == 0: continue
        print("Baris", baris, "- Kursi", kursi)

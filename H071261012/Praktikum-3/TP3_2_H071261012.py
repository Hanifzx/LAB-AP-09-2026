print("--- Setup Denah Bioskop NontonYuk ---")

while True:
    try:
        baris = int(input("Masukkan jumlah baris: "))
        if baris <= 0:
            print("Jumlah baris harus lebih dari 0!")
            continue
    except ValueError:
        print("Input baris harus berupa angka!")
        continue
    break

while True:
    try: 
        kursi = int(input("Masukkan jumlah kursi per baris: "))
        if kursi <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue
    except ValueError:
        print("Input kursi harus berupa angka!")
        continue
    break

print("--- Daftar Kursi Tersedia ---")

for b in range(1, baris + 1):
    for k in range(1, kursi + 1):
        if k == 13:
            continue
        if b == 1 and k % 2 == 0:
            continue
        print(f"Baris {b} - Kursi {k}")
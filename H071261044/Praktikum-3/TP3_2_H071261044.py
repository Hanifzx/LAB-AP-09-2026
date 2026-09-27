# 2. Denah Kursi Bioskop
while True:
    try:
        jumlah_baris = int(input("Masukkan jumlah baris: "))
        if jumlah_baris <= 0:
            print("Jumlah baris harus lebih besar dari 0!")
            print()
            continue
        elif jumlah_baris > 0:  
            jumlah_kursi = int(input("Masukkan jumlah kursi per baris: "))
            if jumlah_kursi <= 0:
                print("Jumlah kursi perbaris harus lebih besar dari 0!")
                print()
                continue
            break
    except:
        print("Input harus berupa angka!")
        print()

print("---Daftar Kursi Tersedia---")
for baris in range(1, jumlah_baris+1):
    for kursi in range(1, jumlah_kursi+1):
        # if kursi == 13:
        #     continue
        # if baris == 1 and kursi % 2 == 0:
        #     continue
        print(f"Baris {baris} - kursi {kursi}")
print("=== Sistem Reservasi PO BUS ===")

while True:
    try:
        maksimal_kursi = int(input("Masukkan maksimal kursi bus: "))
        if maksimal_kursi <= 0:
            print("jumlah Kursi harus lebih besar dari 0")
            print()
        else:  
            break
    except:
        print("Input jumlah kursi harus berupa angka!")

print()
print("--- Sistem Reservasi PO BUS Dimulai ---")
print()

sisa_kursi = maksimal_kursi
total_pendapatan = 0

while sisa_kursi > 0:
    print("Sisa kursi:", sisa_kursi)
    try:
        umur = int(input("Masukkan umur: "))
        if umur < 0:
            print("Umur tidak valid!")
            print()
            continue

        elif umur == 0:
            print("Program dihentikan.")
            break

        elif umur > 0 and umur <= 5:
            kategori = "Balita"
            harga = 0
            print(f"Kategori: {kategori} - Tiket Gratis: {harga}")
            print()
        elif umur >= 6 and umur <= 12:
            kategori = "Anak"
            harga = 50000
            print(f"Kategori: {kategori} - Tiket Gratis: {harga}")
            print()
        else: 
            kategori = "Dewasa"
            harga = 100000
            print(f"Kategori: {kategori} - Harga: {harga}")
            print()

        total_pendapatan += harga
        sisa_kursi -= 1
        print()

    except:
        print("Input umur harus berupa angka!")
        print()

print("--- Semua Kursi Terisi ---")
print("Total pendapatan perjalanan PO BUS kali ini: Rp", total_pendapatan)
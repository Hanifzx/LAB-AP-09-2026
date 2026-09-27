while True:
    try:
        max_kursi = int(input("Masukkan maksimal kursi bus: "))
        if max_kursi <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue
    except ValueError:
        print("Input jumlah kursi harus berupa angka!")
        continue
    break

print()
print("--- Sistem Reservasi PO BUS Dimulai ---")
print()

sisa_kursi = max_kursi
total_pendapatan = 0

while sisa_kursi > 0:
    print(f"Sisa kursi: {sisa_kursi}")

    try:
        umur = int(input("Masukkan umur penumpang: "))
        if umur < 0:
            print("Umur tidak boleh negatif!")
            print()
            continue
        elif umur == 0:
            print("program dihentikan")
            break
        elif 0 < umur <= 5:
            print("Kategori: Balita - Tiket Gratis (Rp 0)")
            harga = 0
        elif 6 <= umur <= 12:
            print("Kategori: Anak - Harga: Rp 50.000")
            harga = 50000
        else:
            print("Kategori: Dewasa - Harga: Rp 100.000")
            harga = 100000
    except ValueError:
        print("Input umur harus berupa angka!")
        print()
        continue

    total_pendapatan += harga
    sisa_kursi -= 1
    print()

print("--- Semua Kursi Terisi ---")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")
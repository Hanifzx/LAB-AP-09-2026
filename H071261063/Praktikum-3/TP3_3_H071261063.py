# CONDITIONAL STATEMENT III

print("=== Sistem Reservasi PO BUS ===")

while True:
    try:
        maksimal_kursi = int(input("Masukkan maksimal kursi bus: "))
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
        umur = int(input("Masukkan umur penumpang(input 0 jika program ingin dihentikan): "))

        if umur < 0:
            print("Umur tidak valid!")
            print()
            continue

        if umur == 0:
            print("Program dihentikan")
            break
    except ValueError:
        print("Input umur harus berupa angka!")
        print()

    if umur <= 5:
        harga = 0
        print(f"Kategori: Balita - Tiket Gratis Rp{harga}")

    elif umur <= 17:
        harga = 50000
        print(f"Kategori: Anak - Harga: Rp{harga}")

    else:
        harga = 100000
        print(f"Kategori: Dewasa - Harga: Rp{harga}")

    total_pendapatan += harga
    sisa_kursi -= 1
    print()

print("--- Semua Kursi Terisi ---")
print("Total pendapatan perjalanan PO BUS kali ini: Rp", total_pendapatan)
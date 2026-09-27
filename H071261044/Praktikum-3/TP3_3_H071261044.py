# 3. Sistem Reservasi "PO BUS"
while True:
    try:
        jumlah_kursi = int(input("Masukkan jumlah kursi: "))
        if jumlah_kursi <= 0:
            print("Jumlah kursi harus lebih besar dari 0!")
            print()
        else:
            break
    except:
        print("Input harus berupa angka bulat!")
        print()
print()
print("===Sistem Reservasi PO BUS Dimulai===")
sisa_kursi = jumlah_kursi
total_pendapatan =  0
while sisa_kursi > 0:
    print(f"Sisa kursi: {sisa_kursi}")
    try: 
        umur = int(input("Masukkan umur: "))
        if umur < 0:
            print("Umur tidak valid!")
            print()
            continue
        elif umur == 0:
            print("Program dihentikan!")
            break
        elif umur >= 1  and umur <= 5:
            kategori = "Balita"
            harga = 0
            print(f"Kategori: {kategori} - Tiket Gratis: {harga}")
            print()
        elif umur >= 6 and umur <= 12:
            kategori = "Anak"
            harga = 50000
            print(f"Kategori: {kategori} - Harga: {harga}")
            print()
        else: 
            kategori = "Dewasa"
            harga = 100000
            print(f"Kategori: {kategori} - Harga: {harga}")
            print()
            
        total_pendapatan += harga
        sisa_kursi -= 1

    except:
        print("Input umur harus berupa angka!")
        print()

print("---Semua Kursi Terisi---")
print(f"Total Pendapatan perjalanan PO BUS kali ini: Rp{total_pendapatan}")


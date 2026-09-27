# 1. Rekapitulasi Transaksi "Dins Store"
print("---Rekapitulasi Transaksi Dins Store---")
print("Ketik '0' Untuk menutup toko dan mengakhiri sesi.")
print()

while True:
    try:
        jumlah_item = int(input("Masukkan jumlah item: "))
        if jumlah_item < 0:
            print("Jumlah tidak boleh negatif")
            print()
        elif jumlah_item > 100:
            print("Maksimal 100 item per transaksi!")
            print()
        elif jumlah_item > 0 and jumlah_item <= 100:
            print(f"Transaksi {jumlah_item} item berhasil")
            print()
        elif jumlah_item == 0:
            print("Toko ditutup. Sesi rekapan selesai!")
            print()
            break
    except:
        print("Input harus berupa angka bulat!")
        print()
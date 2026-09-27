# CONDITIONAL STATEMENT I

print("=== REKAPITULASI TRANSAKSI DINS STORE ===")
print("Ketik 0 untuk menutup toko dan mengakhiri sesi")

while True:
    try:
        jumlah = int(input("Masukkan jumlah item : "))

        if jumlah == 0:
            print("Toko di tutup.Sesi rekap selesai")
            break

        if jumlah < 0:
            print("Jumlah tidak boleh negatif")
            continue

        if jumlah > 100:
            print("Maksimal 100 item per transaksi")
            continue

        print("Transaksi",jumlah,"item berhasil")

    except:
        print("input harus berupa angka")

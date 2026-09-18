jarak = float(input("Masukkan jarak pengiriman (km) : "))

if jarak < 0:
    print("Jarak tidak valid")
else:
    layanan = input("Layanan express (ya/tidak) : ").lower()

    if jarak < 5:
        tarif_dasar = 10000
    elif jarak <= 20:
        tarif_dasar = 20000
    else:
        tarif_dasar = 35000

    biaya_tambahan = 15000 if layanan == "ya" else 0
    total = tarif_dasar + biaya_tambahan
    print(f"Total tarif pengiriman: Rp{total}")
jarak = float(input("Masukkan jarak pengiriman (km): "))

if jarak < 0:
    print("Tidak valid")

else:
    layanan = input("layanan express (ya/tidak): ")

    if jarak < 5:
        tarif = 10000
    elif jarak >= 5 and jarak < 20:
        tarif = 20000
    elif jarak > 20:
        tarif = 35000
    else:
        tarif = 0

    tarif = tarif + 15000 if layanan == "ya" else tarif

    print("Total tarif pengiriman: Rp", tarif)
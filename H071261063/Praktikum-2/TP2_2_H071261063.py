# CONDITIONAL STATEMENT II

jarak = float(input("Masukkan jarak pengiriman (km): "))

if jarak < 0:
    print("Jarak tidak valid")
else:
    express = input("Layanan express (ya/tidak): ")

    if jarak < 5:
        tarif = 10000
    elif jarak <= 20:
        tarif = 20000
    else:
        tarif = 35000

    layanan = 15000 if express == "ya" else 0
    total = tarif + layanan

    print("Total tarif pengiriman : Rp", total)
    
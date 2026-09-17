#variabel jarak dan layanan_ex
Jarak = int(input("Masukkan Jarak Pengiriman (km): "))

if Jarak < 0:
    print("Tidak Valid")
else:
    express = input("Layanan express (ya/tidak): ")

    if Jarak < 5:
        tarif = 10000
    elif Jarak <= 20:
        tarif = 20000
    else:
        tarif = 35000

    layanan = 15000 if express == "ya" else 0
    Tarif_akhir = tarif + layanan

    print("Total tarif pengiriman :", Tarif_akhir)
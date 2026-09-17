#2. Menghitung tarif pengiriman barang
jarak_pengiriman = int(input("Masukkan Jarak Pengiriman(km): "))
if jarak_pengiriman < 0:
    print("Input tidak Valid")
else:
    if jarak_pengiriman < 5:
        tarif = 10000
    elif jarak_pengiriman <= 20:
        tarif = 20000
    else:
        tarif = 35000
    biaya_tambahan = input("Layanan express (ya/tidak): ")
    biaya_express = 15000 if biaya_tambahan == "ya" else 0
    total_tarif = tarif + biaya_express
    print("Total tarif pengiriman: ", total_tarif)
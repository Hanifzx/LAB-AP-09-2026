# Nomor 1
kepedasan = float(input("Masukkan presentase cabai : "))

if kepedasan >= 0 and kepedasan <= 10:
    print("Level Aman")
elif kepedasan >= 11 and kepedasan <= 40:
    print("Level Sedang")
elif kepedasan >= 41 and kepedasan <= 70:
    print("Level Pedas")
elif kepedasan >= 71 and kepedasan <= 100:
    print("Level Ekstrem")
else:
    print("Input tidak valid")

#1. Klasifikasi tingkat kepedasan makanan
tingkat_kepedasan = int(input("Masukkan presentase cabai: "))
if tingkat_kepedasan > 70:
    print("Level Ekstrem")
elif tingkat_kepedasan >= 41 and 70:
    print("Level Pedas")
elif tingkat_kepedasan  >= 11 and 40:
    print("Level Sedang")
elif tingkat_kepedasan >= 0 and 10:
    print("Level Aman")
else:
    print("Input tidak valid")
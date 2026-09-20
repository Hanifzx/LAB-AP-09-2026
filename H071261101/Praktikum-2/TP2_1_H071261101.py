tingkat_kepedasan = int(input("Masukkan Persentase Cabai: "))

if tingkat_kepedasan >= 0 and tingkat_kepedasan <= 10:
    print("Level Aman")
elif tingkat_kepedasan >= 11 and tingkat_kepedasan <= 40:
    print("Level Sedang")
elif tingkat_kepedasan >= 41 and tingkat_kepedasan <= 70:
    print("Level Pedas")
elif tingkat_kepedasan > 70 and tingkat_kepedasan <= 100:
    print("Level Ekstrem")
else:
    print("Tidak Valid")
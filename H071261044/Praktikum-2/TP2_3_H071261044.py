#3. Rekrutmen karyawan baru
nilai_tes_tertulis = int(input("Masukkan nilai tes: "))
if nilai_tes_tertulis < 0:
    print("Tidak Lolos")
elif nilai_tes_tertulis >= 80:
    print("Lolos Wawancara")
elif nilai_tes_tertulis >= 65:
    pengalaman_kerja = int(input("Masukkan Pengalaman Kerja (tahun): "))
    if pengalaman_kerja >= 2:
        print("Lolos bersyarat")
    else:
        print("Tidak Lolos")
else:
    print("Tidak Lolos")
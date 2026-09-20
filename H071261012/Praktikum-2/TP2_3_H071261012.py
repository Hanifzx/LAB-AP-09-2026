nilai_tes = int(input("Masukkan nilai tes: "))

if nilai_tes <65:
   print("Tidak Lolos")
else:  
    pengalaman = int(input("Masukkan pengalaman kerja (tahun): "))
    if nilai_tes >= 80:
        print("Lolos ke Tahap Wawancara")
    elif nilai_tes >= 65 and pengalaman >= 2:
        print("Lolos Bersyarat")
    else:
        print("Tidak Lolos")
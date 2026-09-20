nilai = float(input("Masukkan nilai tes: "))

if nilai <65:
    print("Tidak lolos")
else:
    pengalaman = float(input("Masukkan pengalaman kerja (tahun): "))  
    if nilai >=80:
        print("Lolos ke Tahap Wawancara")
    elif nilai >=65 and pengalaman >=2:
        print("Lolos Bersyarat")
    else:
        print("Tidak Lolos")
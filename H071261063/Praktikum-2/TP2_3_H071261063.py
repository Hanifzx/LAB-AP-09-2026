# CONDITIONAL STATEMENT III

nilai = int(input("Masukkan nilai tes: "))

if nilai < 65:
    print("Tidak Lolos")
else:
    pengalaman = int(input("Masukkan pengalaman kerja (tahun):")) 

    if nilai >= 80:
        print("Lolos Ke Tahap Wawancara")
    elif nilai >= 65 and pengalaman >= 2:
        print("Lolos Bersyarat")
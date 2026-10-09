database = []
def hitung_nilai(*nilai):
    terendah = (min(nilai))
    tertinggi = (max(nilai))
    rata_ratanya = sum(nilai) / len(nilai)
    return rata_ratanya, terendah, tertinggi

while True:
    try:
        masukkan_nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
        if masukkan_nilai == "":
            break
        nilai = float(masukkan_nilai)
        database.append(nilai)
    except:
        print("Tidak ada data")


try:
    rata_rata, terendah, tertinggi = hitung_nilai(*database)
    print(f"Rata-rata kelas: {int(rata_rata)}")
    print(f"Nilai tertinggi: {int(terendah)}")
    print(f"Nilai terendah: {int(tertinggi)}")
except:
    print("Nilai tidak ada")





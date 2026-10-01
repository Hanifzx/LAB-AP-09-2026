database = []
def hitung_nilai(*nilai):
    terendah = (min(nilai))
    tertinggi = (max(nilai))
    rata_rata = sum(nilai) / len(nilai)
    return rata_rata, terendah, tertinggi

while True:
    try:
        masukkan_nilai = float(input("Masukkan nilai ujian siswa (kosongkan untuk selesai): "))
        if masukkan_nilai == "":
            break
       # nilai = float(masukkan_nilai)
        database.append(masukkan_nilai)
    except:
        print("Tidak ada data")

try:
    rata_rata, terendah, tertinggi = hitung_nilai(*database)
    print(f"Rata-rata kelas: {int(rata_rata)}")
    print(f"Nilai tertinggi: {int(tertinggi)}")
    print(f"Nilai terendah: {int(terendah)}")
except:
    print("Nilai tidak ada")
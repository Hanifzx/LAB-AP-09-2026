# #2. Merekap nilai ujian siswa
def hitung_statistika(*nilai):
    rata_rata = sum(nilai) / len(nilai)
    nilai_tertinggi = max(nilai)
    nilai_terendah = min(nilai)
    return rata_rata, nilai_tertinggi, nilai_terendah

daftar_nilai = []
while True:
    input_nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if input_nilai.strip() == "":
        break

    try:
        nilai = float(input_nilai)  
    except:
        print("Input nilai tidak valid! Masukkan angka.")
        continue

    if nilai < 0:
        print("Input nilai tidak valid! Nilai tidak boleh kurang dari 0.")
        continue

    daftar_nilai.append(nilai)

if daftar_nilai:
    rata, tertinggi, terendah = hitung_statistika(*daftar_nilai)

    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")
else:
    print("Data nilai tidak tersedia.")
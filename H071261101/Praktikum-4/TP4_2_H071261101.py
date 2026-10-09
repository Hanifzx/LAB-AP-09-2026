def rekap_nilai(*nilai):
    rata = sum(nilai) / len(nilai)
    max = max(nilai)
    min = min(nilai)
    return rata, max, min


def ke_angka(teks):
    try:
        return int(teks)
    except ValueError:
        return float(teks)


daftar = []
while True:
    try:
        masukan = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
        if masukan == "":
            break
        daftar.append(ke_angka(masukan))
    except:
        print("Input yang anda masukkan tidak valid")
        continue

if len(daftar) == 0:
    print("Data nilai tidak tersedia.")
else:
    rata, tertinggi, terendah = rekap_nilai(*daftar)
    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")
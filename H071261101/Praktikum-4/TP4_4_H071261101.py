def konversi_suhu(suhu, asal, tujuan):
    if asal == "C":
        celsius = suhu
    elif asal == "F":
        celsius = (suhu - 32) * 5 / 9
    else:
        celsius = suhu - 273.15

    if tujuan == "C":
        return celsius
    elif tujuan == "F":
        return celsius * 9 / 5 + 32
    return celsius + 273.15

print("=== Konversi Suhu ===")
while True:
    suhu = input("Masukkan angka suhu (atau 'selesai' untuk keluar): ")
    if suhu == "selesai":
        break

    try:
        suhu = float(suhu)
        asal = input("Skala asal (C/F/K): ").upper()
        tujuan = input("Skala tujuan (C/F/K): ").upper()

        hasil = konversi_suhu(suhu, asal, tujuan)
        print(f"Hasil: {suhu} {asal} = {hasil} {tujuan}")
    except ValueError:
        print("Error: Skala suhu tidak dikenali.")
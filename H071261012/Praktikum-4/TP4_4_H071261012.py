def konversi_suhu(suhu, asal, tujuan):
    if asal not in ("C", "F", "K") or tujuan not in ("C", "F", "K"):
        raise ("Skala suhu tidak dikenali.")

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
    else:
        return celsius + 273.15

print("=== Konversi Suhu ===")
while True:
    masukan = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
    if masukan == "selesai":
        break

    try:
        suhu = float(masukan)
    except:
        print("Error: Suhu harus berupa angka.")
        continue

    skala_asal = input("Skala asal (C/F/K): ")
    skala_tujuan = input("Skala tujuan (C/F/K): ")

    try:
        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)
        print(f"Hasil: {suhu} {skala_asal} = {round(hasil, 2)} {skala_tujuan}")
    except:
        print("Error: Skala suhu tidak dikenali.")
#4. Konversi suhu
def konversi_suhu(nilai, asal, tujuan): 
    asal = asal.upper()
    tujuan = tujuan.upper()

    skala_valid = ['C', 'F', 'K']
    if asal not in skala_valid or tujuan not in skala_valid:
        raise ValueError("Skala suhu tidak dikenali.")

    if asal == 'C':
        celsius = nilai
    elif asal == 'F':
        celsius = (nilai - 32) * 5 / 9
    elif asal == 'K':
        celsius = nilai - 273.15

    if tujuan == 'C':
        return celsius
    elif tujuan == 'F':
        return (celsius * 9 / 5) + 32
    elif tujuan == 'K':
        return celsius + 273.15

print("=== Konversi Suhu ===")

while True:
    input_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
    if input_suhu.lower() == 'selesai':
        break
        
    suhu = float(input_suhu)
    skala_asal = input("Skala asal (C/F/K): ")
    skala_tujuan = input("Skala tujuan (C/F/K): ")
    
    try:
        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)
        print(f"Hasil: {suhu} {skala_asal.upper()} = {hasil} {skala_tujuan.upper()}")
    except ValueError as e:
        print(f"Error: {e}")
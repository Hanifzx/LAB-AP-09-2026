'''Sensor kata'''
ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_kata(teks, kata):
    if kata == "":
        return []
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()
    hasil = []
    start = 0
    while True:
        idx = teks_kecil.find(kata_kecil, start)
        if idx == -1:
            break
        hasil.append(idx)
        start = idx + 1
    return hasil


def cek_batas_kata(teks, i, panjang):
    if i > 0 and teks[i - 1].lower() in ALFABET:
        return False
    akhir = i + panjang
    if akhir < len(teks) and teks[akhir].lower() in ALFABET:
        return False
    return True


def sensor_kata(teks, kata, simbol):
    panjang = len(kata)
    simbol = simbol[0] if simbol != "" else "*"

    indeks_valid = []
    for i in cek_kata(teks, kata):
        if cek_batas_kata(teks, i, panjang):
            indeks_valid.append(i)

    hasil = ""
    pos = 0
    for i in indeks_valid:
        hasil = hasil + teks[pos:i]          
        for _ in range(panjang):             
            hasil = hasil + simbol
        pos = i + panjang
    hasil = hasil + teks[pos:]               
    return (hasil, len(indeks_valid), indeks_valid)


teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")
hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)
print("Hasil Teks:", hasil)
print("Jumlah:", jumlah, "| Indeks:", indeks)
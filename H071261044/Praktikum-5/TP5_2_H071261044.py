#2 Sensor kata
ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_kata(teks, kata):
    hasil = []
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()
    start = 0
    while True:
        idx = teks_kecil.find(kata_kecil, start)
        if idx == -1:
            break
        hasil.append(idx)
        start = idx + 1
    return hasil

def cek_batas_kata(teks, i, panjang):
    if i > 0:
        if teks[i - 1].lower() in ALFABET:
            return False
    akhir = i + panjang
    if akhir < len(teks):
        if teks[akhir].lower() in ALFABET:
            return False
    return True

def sensor_kata(teks, kata, simbol):
    semua_indeks = cek_kata(teks, kata)
    panjang = len(kata)
    hasil = ""
    posisi = 0
    indeks_sensor = []

    for idx in semua_indeks:
        if cek_batas_kata(teks, idx, panjang):
            hasil += teks[posisi:idx] + simbol * panjang
            posisi = idx + panjang
            indeks_sensor.append(idx)

    hasil += teks[posisi:]
    return (hasil, len(indeks_sensor), indeks_sensor)


while True:
    teks = input("Masukkan Teks: ")
    if teks.strip() == "":
        print("Peringatan: Teks tidak boleh kosong, silakan masukkan teks!")
    else:
        break

while True:
    kata = input("Masukkan kata target: ")
    simbol = input("Masukkan simbol: ")

    hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)

    if jumlah == 0:
        print("Peringatan: Kata target tidak valid!")
        print()
        continue
    else:
        print("Hasil Teks:", hasil)
        print("Jumlah:", jumlah, "| Indeks:", indeks)
        break
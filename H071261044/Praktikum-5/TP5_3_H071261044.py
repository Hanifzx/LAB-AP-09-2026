#3 Brute Force Sandi Caesar
ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
    pos = ALFABET.find(ch.lower())
    if pos == -1:
        return ch
    baru = ALFABET[(pos + k) % 26]
    if ch == ch.upper():
        return baru.upper()
    return baru

def mesin_enkripsi(teks, k):
    hasil = ""
    for ch in teks:
        hasil += cek_sandi(ch, k)   
    return hasil

def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

def retas(sandi, kata_kunci):
    hasil = []
    for k in range(26):
        kandidat = mesin_dekripsi(sandi, k)
        if kandidat.lower().find(kata_kunci.lower()) != -1:
            hasil.append((k, kandidat))
    return hasil

sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")

while True:
    kunci = input("Masukkan kata kunci target: ")
    hasil = retas(sandi, kunci)
    if len(hasil) > 0 and kunci.strip() != "":
        break
    print("Kata kunci salah, coba lagi!")
    print()

print("Output Dekripsi:", hasil)
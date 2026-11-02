import re
# aturannya
# diawalu huruf
# isinya huruf, angka, atau underscore saja (spasi tidak boleh)
# panjang 5 sampai 12 karakter (1 huruf awal + 4 sampai 11 karakter lagi)
def cek_username(username):
    pola = r"^[A-Za-z][A-Za-z0-9_]{4,11}$"
    if re.match(pola, username):
        return True
    else:
        return False

daftar_valid = [] #simpah smua usn valid

print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")
print()

while True:
    username = input("Masukkan username: ")

    if username == "SELESAI":
        break

    if cek_username(username):
        print("Username tersedia.")
        daftar_valid.append(username)
    else:
        print("Username tidak valid!")

    print()

print()
print("=== Rekapitulasi ===")
print("Username valid:")

nomor = 1 #memberi nourut pada daftar usn
for nama in daftar_valid:
    print(str(nomor) + ". " + nama)
    nomor = nomor + 1 #tiap loop jalan nomor tmbh 1

print()
print("Jumlah username valid:", len(daftar_valid))
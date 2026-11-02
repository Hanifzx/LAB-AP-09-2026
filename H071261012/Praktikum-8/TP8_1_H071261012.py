import re #mencocokkan teks dgn pola tertentu

# function untuk cek NIM: diawali H071 diikuti 6 angka
def cek_nim(nim):
    pola = r"^H071\d{6}$"
    if re.match(pola, nim):
        return True
    else:
        return False

# function untuk cek email: username@domain.ekstensi
def cek_email(email):
    pola = r"^[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.[A-Za-z]+$"
    if re.match(pola, email):
        return True
    else:
        return False

# function untuk cek nomor telepon: 10 sampai 13 digit angka
def cek_telepon(telepon):
    pola = r"^\d{10,13}$"
    if re.match(pola, telepon):
        return True
    else:
        return False

print("=== Validasi Data Mahasiswa ===")
print()

nim = input("Masukkan NIM       : ")
email = input("Masukkan Email     : ")
telepon = input("Masukkan No. Telp  : ")

print()
print("--- Hasil Validasi ---")

semua_valid = True

if cek_nim(nim):
    print("NIM         : Valid")
else:
    print("Format NIM tidak valid!")
    semua_valid = False

if cek_email(email):
    print("Email       : Valid")
else:
    print("Format email tidak valid!")
    semua_valid = False

if cek_telepon(telepon):
    print("No. Telepon : Valid")
else:
    print("Nomor telepon tidak valid!")
    semua_valid = False

if semua_valid:
    print()
    print("Data mahasiswa berhasil diverifikasi!")  
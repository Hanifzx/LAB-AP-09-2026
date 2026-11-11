import re

def validasi_nim(nim):
    return re.match(r"^H071\d{6}$", nim) is not None

def validasi_email(email):
    return re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}$", email) is not None

def validasi_telp(telp):
    return re.match(r"^\d{10,13}$", telp) is not None

print("=== Validasi Data Mahasiswa ===\n")
nim = input("Masukkan NIM".ljust(18) + ": ")
email = input("Masukkan Email".ljust(18) + ": ")
telp = input("Masukkan No. Telp".ljust(18) + ": ")

nim_ok = validasi_nim(nim)
email_ok = validasi_email(email)
telp_ok = validasi_telp(telp)

print("\n--- Hasil Validasi ---")
print("NIM         :", "Valid" if nim_ok else "Tidak valid")
print("Email       :", "Valid" if email_ok else "Tidak valid")
print("No. Telepon :", "Valid" if telp_ok else "Tidak valid")
print()

if not nim_ok:
    print("Format NIM tidak valid!")

if not email_ok:
    print("Format email tidak valid!")

if not telp_ok:
    print("Nomor telepon tidak valid!")

if nim_ok and email_ok and telp_ok:
    print("\nData mahasiswa berhasil diverifikasi!")
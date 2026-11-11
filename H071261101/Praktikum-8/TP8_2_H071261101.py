import re

def validasi_username(username):
    return re.match(r"^[A-Za-z][A-Za-z0-9_]{4,11}$", username) is not None

print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.\n")

username_valid = []

while True:
    username = input("Masukkan username: ")

    if username == "SELESAI":
        break

    if validasi_username(username):
        print("Username tersedia.\n")
        username_valid.append(username)
    else:
        print("Username tidak valid!\n")

print("\n=== Rekapitulasi ===")
print("Username valid:")
for i, nama in enumerate(username_valid, start=1):
    print(f"{i}. {nama}")

print(f"\nJumlah username valid: {len(username_valid)}")
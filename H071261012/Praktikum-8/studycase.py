import re

pattern = r"^[A-Z]{1}[a-z]{3}-(X99|Y88|Z77){1}[\d]{2,4}[(*|+|$]{2}$"
daftar_password = [

"Kzxc-X9912*$",

"Bqwe-Z771234++",

"Kzx-X9912*$",

"kzxc-X9912*$",

"Kzxc-A1112*$",

"Bqwe-Z7712345++",

"Kzxc-X9912*",

"Kzxc-X9912ab"

]

print("=== SISTEM KEAMANAN PASSWORD ===")

for password in daftar_password:
    hasil = re.match(pattern, password)
    if hasil:
        print(f"[AKSES DITERIMA]: {password}")
    else:
        print(f"[AKSES DITOLAK]: {password}")
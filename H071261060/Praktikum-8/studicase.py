import re

daftar_password = [
    "Kzxc-X9912*$",
    "Bqwe-Z771234++",
    "Kzx-X9912*$",
    "kzxc-X9912*$",
    "Bqwe-Z7712345++",
    "Kzxc-X9912*",
    "Kzxc-X9912ab",
]

paterrn = r"^[A-Za-z]{3}-(X99|Y88|Z77).{2,4}[\*|\+|\$]{2}$"

for i in daftar_password:
    result = re.match(paterrn, i)
    if result:
        print(f"[AKSES DITERIMA] : {i}")
    else:
        print(f"[AKSES DITOLAK] : {i}")
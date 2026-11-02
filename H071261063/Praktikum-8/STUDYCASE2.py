import re

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

patern = r'^[A-Z]{1,1}+[a-z]{3,3}+[-]+["X99"|"Y88"|"Z77"]+\d{2,4}+[*+$]{2,2}$'

for a in daftar_password:
    result = re.match(patern, a)
    if result:
        hasil = "Valid"
    else:
        hasil = "Tidak Valid"

    print(hasil)
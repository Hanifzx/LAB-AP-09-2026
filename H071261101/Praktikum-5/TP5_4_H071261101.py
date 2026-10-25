DOMAIN_RESMI = (".com", ".id", ".ac.id")


def deteksi_anomali_email(email):
    error = []

    if email.count("@") != 1:
        error.append("Harus memiliki tepat satu karakter @.")
        if " " in email:
            error.append("Tidak boleh mengandung spasi.")
        return error

    local, domain = email.split("@")

    if local == "" or domain == "":
        error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    if " " in email:
        error.append("Tidak boleh mengandung spasi.")

    if local != "" and (local[0] == "." or local[-1] == "." or ".." in local):
        error.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")

    if "." not in domain:
        error.append("Bagian domain wajib memiliki minimal satu titik.")
    if domain != "" and (".." in domain or domain[-1] == "."):
        error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    if not email.lower().endswith(DOMAIN_RESMI):
        error.append("Wajib berakhiran .com, .id, atau .ac.id")

    return error


def cetak_daftar(daftar_email_valid, karakter_border):
    lebar = 0
    for email in daftar_email_valid:
        if len(email) > lebar:
            lebar = len(email)

    garis = "+" + karakter_border * (lebar + 2) + "+"
    baris = [garis]
    for email in daftar_email_valid:
        padding = " " * (lebar - len(email))
        baris.append("| " + email + padding + " |")
    baris.append(garis)
    return "\n".join(baris)


def sudah_terdaftar(email, daftar):
    for e in daftar:
        if e.lower() == email.lower():
            return True
    return False


print("--- Sistem Pencatatan email valid ---")
border = input("Masukkan border dengan karakter bebas: ")
border = border[0] if border != "" else "="
print()
print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")
daftar_valid = []
while True:
    email = input("Masukkan email: ")
    if email.strip().lower() == "tutup":
        break
    error = deteksi_anomali_email(email)
    if sudah_terdaftar(email, daftar_valid):
        error.append("Email sudah terdaftar (Duplikat).")
    if error:
        print(">> Email DITOLAK karena:")
        for e in error:
            print("   - " + e)
    else:
        daftar_valid.append(email)
        print(">> Email VALID!")
print()
print("--- HASIL EMAIL VALID ---")
if daftar_valid:
    print(cetak_daftar(daftar_valid, border))
else:
    print("(Tidak ada email valid yang tercatat)")
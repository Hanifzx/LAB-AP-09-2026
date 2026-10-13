#4. Validasi Email
def deteksi_anomali_email(email):
    pelanggaran = []

    #Aturan 1: Hanya boleh satu @
    if email.count("@") != 1:
        pelanggaran.append("Harus memiliki tepat satu karakter '@'. ")
        return pelanggaran

    local, domain = email.split("@")

    #Aturan 2: local dan domain tidak boleh kosong
    if local == "" or domain == "":
        pelanggaran.append(
            "Bagian sebelum '@' (local) atau Setelah '@' (domain) tidak boleh kosong!"
            )

    #Aturan 3: tidak boleh terdapat spasi
    if " " in email:
        pelanggaran.append("Tidak boleh mengandung spasi!")

    #Aturan 4: aturan titik pada local
    if local.startswith(".") or local.endswith(".") or ".." in local:
        pelanggaran.append(
            "Bagian local tidak boleh diawali atau di akhiri titik, "
            "dan tidak boleh mengandung titik berurutan!"
        )

    #Aturan 5: aturan titik pada domain
    if "." not in domain:
        pelanggaran.append("Bagian domain wajib memiliki minimal satu titik!")
    if ".." in domain or domain.endswith ("."):
        pelanggaran.append(
            "Bagian domain tidak boleh mengandung titik berurutan atau di akhiri titik!"
        )

    #Aturan 6: akhiran resmi
    kecil = email.lower()
    if not (kecil.endswith(".com") or kecil.endswith(".id") or kecil.endswith(".ac.id")):
        pelanggaran.append("Wajib berakhiran dengan '.com', '.id', atau '.ac.id'!")

    return pelanggaran

def sudah_terdaftar(email, daftar_email_valid):
    for sudah in daftar_email_valid:
        if sudah.lower() == email.lower():
            return True
    return False

def cetak_daftar(daftar_email_valid, karakter_border):
    terpanjang = 0
    for email in daftar_email_valid:
        if len(email) > terpanjang:
            terpanjang = len(email)

    garis = "+" + karakter_border * (terpanjang + 2) + "+"

    hasil = garis + "\n"
    for email in daftar_email_valid:
        padding = " " * (terpanjang - len(email))
        hasil += "| " + email + padding + " |\n"
    hasil += garis
    return hasil

def baca_border():
    border = input("Masukkan karakter bebas untuk border: ")
    if border == "":
        return "="
    return border[0]

def main():
    daftar_valid = []
    border = "="

    try:
        print("--- Sistem Pencatatan email valid ---")
        border = baca_border()
        print()
        print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

        while True:
            email = input("Masukkan email: ")
            if email.strip().lower() == "tutup":
                break

            masalah = deteksi_anomali_email(email)
            if len(masalah) == 0 and sudah_terdaftar(email, daftar_valid):
                masalah.append("Email sudah terdaftar (Duplikat). ")

            if len(masalah) > 0:
                print(">> Email DITOLAK karena: ")
                for pesan in masalah:
                    print("   - " + pesan)
            else:
                daftar_valid.append(email)
                print(">> Email VALID!")
    except (EOFError, KeyboardInterrupt):
        print("Input dihentikan.")

    print()
    print("--- HASIL EMAIL VALID ---")
    if len(daftar_valid) == 0:
        print("(Belum ada email valid tercatat.)")
    else:
        print(cetak_daftar(daftar_valid, border))

if __name__ == "__main__":
    main()
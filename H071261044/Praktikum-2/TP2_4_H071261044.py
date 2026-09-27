# 4. Aplikasi pemesanan tiket perjalanan
tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ")
waktu = input("Masukkan waktu (Pagi/Malam): ")
tipe_pengunjung = input("Masukkan tipe pengunjung (Anak/Dewasa): ")
match tujuan:
    case "Pantai":
        if waktu == "Pagi" and (tipe_pengunjung == "Anak" or tipe_pengunjung == "Dewasa"):
            print("Paket Rekomendasi: Paket A")
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case "Pegunungan":
        if waktu == "Pagi" and tipe_pengunjung == "Dewasa":
            print("Paket Rekomendasi: Paket B")
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case "Kota":
        if waktu == "Malam" and (tipe_pengunjung == "Anak" or tipe_pengunjung == "Dewasa"):
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case _:
        print("Tempat tidak tersedia.")
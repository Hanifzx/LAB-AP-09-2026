# Nomor 4
tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota) : ")
waktu = input("Masukkan waktu (Pagi/Malam) : ")
tipe_pengunjung = input("Masukkan tipe penunjung (Anak/Dewasa) : ")

match tujuan :
    case "Pantai" :
        if waktu == "Pagi":
            if tipe_pengunjung == "Anak" or tipe_pengunjung == "Dewasa":
                print("Paket A")
            else :
                print("Tidak ada paket yang cocok")
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa" :
            print("Paket C")
        else :
            print("Tidak ada paket yang cocok")
    case "Pegunungan" :
        if waktu == "Pagi":
            if tipe_pengunjung == "Dewasa":
                print("Paket B")
            else :
                print("Tidak ada paket yang cocok")
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa" :
            print("Paket C")
        else :
                print("Tidak ada paket yang cocok")
    case "Kota" :
        if waktu == "Malam":
            if tipe_pengunjung == "Dewasa":
                print("Paket C")
            else:
                print("Tidak ada paket yang cocok")
        else:
            print("Tidak ada paket yang cocok")
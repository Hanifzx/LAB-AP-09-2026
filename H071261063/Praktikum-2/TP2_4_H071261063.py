# CONDITIONAL STATEMENT IV

tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ")
waktu = input("Masukkan waktu (Pagi/Malam): ")
tipe_pengunjung = input ("Masukkan tipe pengunjung (Anak/Dewasa): ")

match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            rekomendasi = "Paket A"
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa":
            rekomendasi = "Paket C"
        else:
            rekomendasi = "Paket Tidak Tersedia" 
                 
    case "Pegunungan":
        if waktu == "Pagi" and tipe_pengunjung == "Dewasa":
            rekomendasi = "Paket B"
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa":  
            rekomendasi = "Paket C"
        else:
            rekomendasi = "Paket Tidak Tersedia"
        
    case "Kota":
        if waktu == "Malam" and tipe_pengunjung == "Dewasa":
            rekomendasi = "Paket C"
        else:
            rekomendasi = "Paket Tidak Tersedia" 
        
print("Paket Rekomendasi: ", rekomendasi)

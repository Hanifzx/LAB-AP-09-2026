waktu = ("Senin","23:00")

print("Jam Kejadian: ",waktu[1])

Tersangka = ["Andi", "Budi", "Citra"]

Tersangka.append("Dina")
Tersangka.remove("Budi")

print("Daftar tersangka baru: ",Tersangka)

bukti_tkp = {"Rambut","Jejak Sepatu", "Kacamata"}
barang_dina = {"Buku","Jejak Sepatu", "Pena"}

print("Buktu yang memberatkan Dina: ",bukti_tkp & barang_dina)

status_akhir = {
    "Andi": "Aman",
    "Citra": "Aman",
    "Dina": "Buron"
}

status_akhir["Dina"]="Tertangkap"

print("Status Akhir:",status_akhir)

waktu = ("Senin", "23:00")
tersangka = {"Andi", "Budi", "Citra"}
tersangka.add("Dina")
tersangka.remove("Budi")
set_bukti_tkp = {"Rambut", "Jejak Sepatu", "Kacamata"}
barang_dina = {"Buku", "Jejak Sepatu", "Pena"}
status = {
    "Andi": "Aman",
    "Citra": "Aman",
    "Dina": "Tertangkap"
}

print(f"Jam kejadian: {waktu[1]}")
print(f"Daftar tersangka baru: {tersangka}")
print(f"Bukti yang memberatkan Dina: {set_bukti_tkp & barang_dina}")
print(f"Status Akhir: {status}")
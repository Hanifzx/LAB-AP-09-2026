waktu = ("senin", "23.00")
print(f"jam kejadian : {waktu[1]}")

tersangka = ["andi", "budi", "citra"]
tersangka.append("dina")
tersangka.remove("budi")
print(f"daftar tersangka baru : {tersangka}")

bukti_tkp = {"rambut", "jejak sepatu", "kacamata"}
barang_dina = {"buku", "jejak sepatu", "pena"}
bukti_memberatkan = bukti_tkp.intersection(barang_dina)
print(f"bukti yang memberatkan dina: {bukti_memberatkan}")

status = {"andi": "aman", "citra": "aman", "dina": "buron"}
status["dina"] = "ditangkap"
print(f"status akhir: {status}")

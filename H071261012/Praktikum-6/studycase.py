jam = ("senin", "23:00")
tersangka = ["andi", "budi", "citra"]

tersangka.append("dina")
tersangka.remove("budi")

bukti =  {"rambut", "jejaksepatu", "kacamata"}
dina = {"buku", "jejaksepatu", "pena"}
bukti_pemberat = bukti.intersection(dina)

print(f"jam: {jam[1]}")
print(f"tersangka baru: {tersangka}")
print(f"bukti memberatkan dina: {bukti_pemberat}")

status = {"andi": "aman", "citra": "aman", "dina": "buronan"}
status["dina"] = "tertangkap!"
print(f"status akhir: {status}")

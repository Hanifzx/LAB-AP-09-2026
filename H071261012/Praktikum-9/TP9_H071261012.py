class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        skor = (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)
        return skor

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self, nomor):
        skor = self.hitung_skor_akhir()
        status = self.status_performa()
        print(f"| {nomor:<3} | {self.nama:<10} | {self.id_pemain:<11} | {self.role:<9} | {skor:<10.2f} | {status:<13} |")

print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
print()

daftar_pemain = []
jumlah = int(input("Masukkan jumlah pemain: "))

for i in range(jumlah):
    print()
    print(f"-- Data Pemain ke-{i + 1} --")
    nama = input("Nama: ")
    id_pemain = input("ID Pemain: ")
    role = input("Role: ")
    kill = int(input("Nilai Kill: "))
    assist = int(input("Nilai Assist: "))
    objective = int(input("Nilai Objective: "))

    #bikin objek pemain, init otomatis jalan & simpan keenam data ke objek baru
    pemain = Pemain(nama, id_pemain, role, kill, assist, objective)
    daftar_pemain.append(pemain)

print()
print("=== REKAPITULASI PERFORMA PEMAIN ===")
print("=" * 75)
print(f"| {'No':<3} | {'Nama':<10} | {'ID Pemain':<11} | {'Role':<9} | {'Skor Akhir':<10} | {'Status':<13} |")
print("=" * 75)

nomor = 1
for p in daftar_pemain:
    p.tampilkan_data(nomor)
    nomor += 1

print("=" * 75)
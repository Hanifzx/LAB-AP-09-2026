class Pemain:
    def __init__ (self, Nama_Pemain, ID_Pemain, Role, Nilai_kill, Nilai_Assist, Nilai_Objective):
        self.Nama_Pemain = Nama_Pemain
        self.ID_Pemain = ID_Pemain 
        self.Role = Role
        self.Nilai_Kill = Nilai_kill
        self.Nilai_Assist = Nilai_Assist
        self.Nilai_Objective = Nilai_Objective
        self.level = self.tentukan_level()

    def tentukan_level (self):
        Skor = self.hitung_skor_akhir()
        if Skor >= 85:
            return "Diamond"
        elif Skor >= 70:
            return "Platinum"
        elif Skor >= 60:
            return "Gold"
        else:
            return "Bronze"

    def hitung_skor_akhir (self):
        return (0.3 * self.Nilai_Kill) + (0.3 * self.Nilai_Assist) + (0.4 * self.Nilai_Objective)

    def status_performa (self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        return "Perlu Evaluasi"

    def tampilkan_data (self, no):
        print(f"| {no:<3} | {self.Nama_Pemain:<10} | {self.ID_Pemain:<10} | {self.Role:<10} | "
              f"{self.hitung_skor_akhir():<10.2f} | {self.status_performa():<14} | {self.level:<10} |")

print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
print()
while True:
    jumlah = (input("Masukkan jumlah pemain: "))
    if jumlah == "":
        print("Jumlah Tidak Boleh Kosong")
        continue
    jumlah = int(jumlah)
    break

daftar_pemain = []

for i in range(jumlah):
    print()
    print(f"-- Data Pemain ke-{i + 1} --")
    nama = input("Nama: ")
    id_pemain = input("ID Pemain: ")
    role = input("Role: ")
    kill = float(input("Nilai kill: "))
    assist = float(input("Nilai Assist: "))
    objective = float(input("Nilai Objective: "))

    pemain = Pemain(nama, id_pemain, role, kill, assist, objective)
    daftar_pemain.append(pemain)

print()
print("=== REKAPITULASI PERFORMA PEMAIN ===")
print("="*89)
print(f"| {'No':<3} | {'Nama':<10} | {'ID Pemain':<10} | {'Role':<10} | "
      f"{'Skor Akhir':<10} | {'Status':<14} | {'level':<10} | " )
print("="*89)
for no, pemain in enumerate(daftar_pemain, start=1):
    pemain.tampilkan_data(no)
print("="*89)
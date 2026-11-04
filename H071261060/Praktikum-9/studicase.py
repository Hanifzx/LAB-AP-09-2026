class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        return (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)

    def status_peforma(self):
        skor = self.hitung_skor_akhir()
        if skor >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self):
        skor = self.hitung_skor_akhir()
        status = self.status_peforma()
        return f" {self.nama}".ljust(12) + " | " + self.id_pemain.ljust(10) + " | " + self.role.ljust(10) + " | " + f"{skor}".ljust(10) + " | " + status.ljust(16) + " |"

    def get_id(self): # Method ini digunakan untuk mengambil id
        return self.id_pemain

    def pemain_ditemukan(self): # Method ini digunakan untuk mengeluarkan ouput dari pemain yang dicari
        print("\nNama".ljust(12) + f": {self.nama}")
        print("ID".ljust(12) + f": {self.id_pemain}")
        print("Role".ljust(12) + f": {self.role}")
        print("Skor Akhir".ljust(12) + f": {self.hitung_skor_akhir()}")
        print("Status".ljust(12) + f": {self.status_peforma()}")

data_pemain = []

print("--- SISTEM PENILAIAN PEFORTMA PEMAIN ---")

while True:
    print("\nPilihan:")
    print("1. Menambahkan Pemain")
    print("2. Mencari Pemain")
    print("3. Statistik Pertandingan")
    print("4. Selesai")
    try:
        pilihan = int(input("Masukkan pilihan: "))
    except:
        print("Input yang anda masukkan tidak valid!")
    if pilihan == 1:
        while True:
            try:
                jumlah_pemain = int(input("\nMasukkan jumlah pemain: "))
                if jumlah_pemain <= 0:
                    print("Jumlah pemain harus lebih dari 0!")
                    continue
                else:
                    pemain = 1
                    while pemain < jumlah_pemain + 1:
                        try:
                            print(f"\n-- Data Pemain ke-{pemain} --")
                            data_nama = input("Nama".ljust(16) + ": ")
                            data_id = input("ID Pemain".ljust(16) + ": ")
                            data_role = input("Role".ljust(16) + ": ")
                            data_kill = int(input("Nilai Kill".ljust(16) + ": "))
                            data_assist = int(input("Nilai Assist".ljust(16) + ": "))
                            data_objective = int(input("Nilai Objective".ljust(16) + ": "))
                            isi_data_pemain = Pemain(data_nama, data_id, data_role, data_kill, data_assist, data_objective)
                            data_pemain.append(isi_data_pemain)
                            pemain += 1
                        except:
                            print("Input yang anda masukkan tidak valid!")
                            continue
                    break
            except:
                print("Input yang anda masukkan tidak valid!")
                continue
    elif pilihan == 2: #Conditional untuk pilihan ke 2, yang dimana disini terdapat looping untuk mengecek pengecekan id yang ingin dicari
        print("\n=== PENCARIAN PEMAIN ===")
        id_dicari = input("\nMasukkan ID yang ingin dicari: ")
        maka_ditemukan = False
        for i in data_pemain:
            if i.get_id() == id_dicari:
                print("\nData Pemain Ditemukan!")
                i.pemain_ditemukan()
                maka_ditemukan = True
        if maka_ditemukan == False:
            print("Pemain tidak ditemukan!")
    elif pilihan == 3: #Conditional untuk pilihan ke 3, disini terdapat looping untuk menambahkan variable-variable yang sesuai
        total_pemain = 0
        pemain_unggul = 0
        pemain_evaluasi = 0
        rata_rata_skor = 0
        for i in data_pemain:
            if i.status_peforma() == "Unggul":
                pemain_unggul += 1
            elif i.status_peforma() == "Perlu Evaluasi":
                pemain_evaluasi += 1
            rata_rata_skor += i.hitung_skor_akhir()
            total_pemain += 1
            print("Total Pemain".ljust(12) + f": {total_pemain}")
            print("Pemain Unggul".ljust(12) + f": {pemain_unggul}")
            print("Pemain Evaluasi".ljust(12) + f": {pemain_evaluasi}")
            print("Rata-rata Skor".ljust(12) + f": {rata_rata_skor / total_pemain}")
    elif pilihan == 4: #Conditional ke 4 ini untuk keluar dari pilihan
        break
    else:
        print("Input yang anda masukkan tida valid!")
        continue

print("\n--- REKAPITULASI PERFORMA PEMAIN ---")
print("=" * 78)
print("| " + "No".ljust(3) + "|" + " Nama".ljust(12) + " | " + "ID Pemain".ljust(10) + " | " + "Role".ljust(10) + " | " + "Skor Akhir".ljust(10) + " | " + "Status".ljust(16) + " |")
print("=" * 78)
for i, isi in enumerate(data_pemain, start=1):
    print(f"| {i}  |" + isi.tampilkan_data())
print("=" * 78)
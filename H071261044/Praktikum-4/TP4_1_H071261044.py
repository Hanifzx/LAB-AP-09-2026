#1. Kasir sederhana
def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal -= subtotal * 0.10
    return int(subtotal)

print("Selamat datang di Kasir Minimarket!")
while True:
    status_member = input("Apakah anda member? (y/n): ").strip().lower()
    is_member = None
    if status_member == 'y':
        is_member = True
        break
    elif status_member == 'n':
        is_member = False
        break
    else:
        print("Input tidak valid!")

total_belanja = 0
while True:
    try:
        nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
        if nama_barang == "":
            break

        harga = int(input("Harga barang: "))
        if harga < 0:
            raise ValueError("Harga tidak valid!")
        jumlah = int(input("Jumlah barang: "))
        if jumlah < 0:
            raise ValueError("Jumlah tidak valid")
        subtotal = hitung_subtotal(harga, jumlah, is_member)
        total_belanja += subtotal

        print(f"Subtotal {nama_barang}: Rp{subtotal}")
        print(f"Total belanja: Rp{total_belanja}")

    except:
        print("Tidak valid!")

subtotal = 0
def sistem(harga, jumlah, adalah_member=False):
    total_belanja = harga * jumlah
    if adalah_member:
        diskon = total_belanja * (1 - 0.10)
        return diskon
    return total_belanja

print("Selamat datang di kasir Minimarket!")
while True:
    apakah_member = input("Apakah Anda member? (y/n): ")
    if apakah_member != "y" and apakah_member != "n":
        print("Input yang anda masukkan salah")
        continue
    member = apakah_member == "y"
    break

while True:
    try:
        barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
        if barang == "selesai":
            print(f"Total belanja: Rp{subtotal}")
            break
        harga_barang = int(input("Harga barang: "))
        jumlah_barang = int(input("Jumlah barang: "))
        if member:
            sub_total = sistem(harga_barang, jumlah_barang, adalah_member=True)
        if not member:
            sub_total = sistem(harga_barang, jumlah_barang,)
        subtotal = subtotal + sub_total
        print(f"Subtotal {barang}: Rp{sub_total}")
    except:
        print("Input yang anda masukkan salah")
        continue
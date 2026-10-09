#3. Hitung mundur simulasi 
def hitung_mundur(n):
    print(n)
    if n == 0:
        print("Luncurkan")
        return
    hitung_mundur(n-1)

while True:
    try:
        angka = int(input("Masukkan angka awal hitung mundur: "))
        if angka < 0:
            print("Input tidak valid, angka tidak boleh negatif. ")
        else:
            hitung_mundur(angka)
        break
    except: 
        print("Input harus angka bulat!")

def hitung_mundur(n):
    if n == 0:
        print(n)
        print("Luncurkan!")
    else:
        print(n)
        hitung_mundur(n -1)


while True:
    try:
        angka = int(input("Masukkan angka awal hitung mundur: "))
        if angka < 0:
            print("error")
        else:
            break
        
        
    except:
        print("Input yang anda masukkan tidak valid")
        continue

hitung_mundur(angka)
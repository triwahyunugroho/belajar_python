while True:
    angka = input("masukkan angka : ")
    try:
        angka = int(angka)

    except Exception:
        print("angka tidak valid")

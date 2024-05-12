while True:
    angka = input("masukkan angka : ")
    try:
        angka = int(angka)
        if angka <= 0:
            print("program selesai")
            break

        list_ganjil = []
        list_genap = []

        cek_angka = 1
        ganjil = True

        print("==========================================")
        while cek_angka <= angka:
            if ganjil:
                print("#periksa", cek_angka, ": adalah bilangan ganjil")
                list_ganjil.append(cek_angka)
                print("list_ganjil :", list_ganjil)
                ganjil = False
            else:
                print("#periksa", cek_angka, ": adalah bilangan genap")
                list_genap.append(cek_angka)
                print("list_genap :", list_genap)
                ganjil = True
            cek_angka = cek_angka+1
            print("---------------------------------------")

        print("bilangan ganjil dari 1 sampai", angka, "adalah", list_ganjil)
        print("bilangan genap dari 1 sampai", angka, "adalah", list_genap)

    except Exception:
        print("angka tidak valid")
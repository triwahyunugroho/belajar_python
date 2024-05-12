saldo = 1000

tarik_tunai = input("Tarik Tunai : ")

try:
    tarik_tunai = int(tarik_tunai)
    print("=================================")
    print("saldo awal :", saldo)
    print("tarik tunai :", tarik_tunai)
    print("saldo akhir :", saldo-tarik_tunai)
    print("=================================")
except Exception:
    print("angka tidak valid")

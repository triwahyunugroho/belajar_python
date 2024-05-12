saldo = input("Saldo : ") #saldo adalah string
tarik_tunai = input("Tarik tunai : ") #tarik_tunai adalah string

saldo = int(saldo) #saldo adalah int
tarik_tunai = int(tarik_tunai) #tarik_tunai adalah int

print("=================================")
print("saldo awal :", saldo)
print("tarik tunai :", tarik_tunai)
print("saldo akhir :", saldo-tarik_tunai)
print("=================================")

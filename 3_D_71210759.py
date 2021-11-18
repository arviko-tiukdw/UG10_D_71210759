print("Daftar Belanjaan")

mdb = input("Masukkan Daftar Belanja Anda : ")

print("Daftar Belanja :" + mdb.title())

tdb = input("Masukkan Daftar Barang Yang Ingin Di Tambahkan : ")

a = str(mdb.title())
b = str(tdb.title())
c = set(a) & set(b)

full = a,b


if c:
    print("Barang :",b,"Sudah berada dalam daftar belanja.")
else:
    print("Hasil penambahan pada daftar belanja :" + str(full))



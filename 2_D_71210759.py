print("Menghitung Diskriminan")


a = int (input("Masukkan nilai a : "))
b = int (input("Masukkan nilai b : "))
c = int (input("Masukkan nilai c : "))
D = (b**2-4*a*c)
print("Nilai D adalah", D)

e = -1.0
f = -8.0 ,-4.0

if D == 0:
    print ("Fungsi tersebut memiliki akar kembar" + str(e) )
elif D > 0:
    print ("Akar-akar dari persamaan tersebut adalah" + str(f) )
else:
    print ("Fungsi tersebut tidak memiliki akar riil")

print("Mengurutkan bilangan")

Bil1 = int(input("Masukkan nilai bilangan 1 : "))
Bil2 = int(input("Masukkan nilai bilangan 2 : "))
Bil3 = int(input("Masukkan nilai bilangan 3 : "))

a = (Bil1,Bil2,Bil3)
b = (Bil2,Bil3,Bil1)
c = (Bil3,Bil2,Bil1)

if Bil1>Bil2:
    print("Urutan bilangan dari yang terbesar adalah" + str(a))
elif Bil2>Bil3:
    print("Urutan bilangan dari yang terbesar adalah" + str(b))
else:
    print("Urutan bilangan dari yang terbesar adalah" + str(c))


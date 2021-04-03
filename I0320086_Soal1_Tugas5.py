# Input nama dan jenis kelamin
nama = input("Masukkan Nama :")
jk = input("Jenis Kelamin (L/P) :")
# Buat percabangan dan output masing-masing
if jk == "L" :
    print("Selamat datang, Bapak",nama,"!")
elif jk == "P" :
    print("Selamat datang, Ibu",nama,"!")
else :
    print("Masukkan data dengan benar!")
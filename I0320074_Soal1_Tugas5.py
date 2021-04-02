# Input nama dan jenis kelamin
nama = input("Masukkan Nama :")
kelamin = input("Jenis Kelamin (L/P) :")
# Buat percabangan dan output masing-masing
if kelamin == "L" :
    print("Selamat datang, Tuan",nama,"!")
elif kelamin == "P" :
    print("Selamat datang, Nyonya",nama,"!")
else :
    print("Masukkan data dengan benar!")
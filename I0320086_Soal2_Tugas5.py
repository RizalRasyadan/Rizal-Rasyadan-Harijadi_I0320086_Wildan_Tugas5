# Input nama dan nilai angka
nama = input("Masukkan Nama :")
nilai = float(input("Masukkan Nilai Angka:"))
# Buat percabangan
if nilai >= 86 :
    konversi = "A"
elif nilai >= 82 :
    konversi = "A-"
elif nilai >= 77 :
    konversi = "B+"
elif nilai >= 68 :
    konversi = "B"
elif nilai >= 65 :
    konversi = "C+"
elif nilai >= 60 :
    konversi = "C"
else :
    konversi = "E"
# Print hasil output
print("Halo,",nama,"! Nilai anda setelah dikonversi adalah",konversi)
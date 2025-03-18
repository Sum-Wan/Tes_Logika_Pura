from collections import Counter

 # Pembuatan logo perusahaan
def logo_perusahaan(nama_perusahaan):
    # Menghitung frekuensi tiap karakter
    frekuensi = Counter(nama_perusahaan)
    
    # Mengurutkan berdasarkan frekuensi tiap karakter, jika sama urutkan berdasarkan alfabet
    urutkan = sorted(frekuensi.items(), key=lambda x: (-x[1], x[0]))
    
    # Mengambil 3 karakter pertama
    logo = ''.join([item[0] for item in urutkan[:3]])
    
    # Menampilkan hasil
    print("Logo perusahaan = {logo}")

# Input
nama_perusahaan = input("Masukkan nama perusahaan: ")

# Menjalankan fungsi
logo_perusahaan(nama_perusahaan)
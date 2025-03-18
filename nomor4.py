# konversi integer menjadi format rupiah & nominal
def terbilang(angka):
    satuan = ["", "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan", "sepuluh", "sebelas"]
    
    if angka < 12:
        return satuan[angka]
    elif angka < 20:
        return terbilang(angka - 10) + " belas"
    elif angka < 100:
        return terbilang(angka // 10) + " puluh" + (" " + terbilang(angka % 10) if angka % 10 != 0 else "")
    elif angka < 200:
        return "seratus" + (" " + terbilang(angka - 100) if angka > 100 else "")
    elif angka < 1000:
        return terbilang(angka // 100) + " ratus" + (" " + terbilang(angka % 100) if angka % 100 != 0 else "")
    elif angka < 2000:
        return "seribu" + (" " + terbilang(angka - 1000) if angka > 1000 else "")
    elif angka < 1000000:
        return terbilang(angka // 1000) + " ribu" + (" " + terbilang(angka % 1000) if angka % 1000 != 0 else "")
    elif angka < 1000000000:
        return terbilang(angka // 1000000) + " juta" + (" " + terbilang(angka % 1000000) if angka % 1000000 != 0 else "")
    else:
        return "Angka terlalu besar"

def format_rupiah(angka):
    return f"Rp. {angka:,} ,-".replace(",", ".")

# Menjalankan fungsi
if __name__ == "__main__":
    input_angka = int(input("Masukkan nominal angka: "))
    print(format_rupiah(input_angka))
    print(terbilang(input_angka) + " rupiah")
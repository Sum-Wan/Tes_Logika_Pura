#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <cctype>

// Menghitung frekuensi karakter 
using namespace std;

void proses_string(const string& input_str) {
    unordered_map<char, int> frekuensi;

    // Menghitung frekuensi tiap karakter (angka dan huruf)
    for (char ch : input_str) {
        frekuensi[ch]++;
    }

    // Menampilkan hasil dalam format (jumlah, karakter) diurutkan berdasarkan karakter
    // Mengurutkan karakter dalam urutan alfanumerik (angka, huruf kecil, huruf besar)
    for (char ch = '0'; ch <= '9'; ch++) {
        if (frekuensi.find(ch) != frekuensi.end()) {
            cout << "(" << frekuensi[ch] << "," << ch << ")";
        }
    }

    for (char ch = 'a'; ch <= 'z'; ch++) {
        if (frekuensi.find(ch) != frekuensi.end()) {
            cout << "(" << frekuensi[ch] << "," << ch << ")";
        }
    }

    for (char ch = 'A'; ch <= 'Z'; ch++) {
        if (frekuensi.find(ch) != frekuensi.end()) {
            cout << "(" << frekuensi[ch] << "," << ch << ")";
        }
    }

    cout << endl;
}

int main() {
    string input_str;
    cout << "Masukkan string: ";
    cin >> input_str;

    // menjalankan fungsi
    proses_string(input_str);

    return 0;
}
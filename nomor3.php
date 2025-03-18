<?php

// Konversi tipe data
function convert_numbers($n) {
    // Menentukan lebar padding berdasarkan angka terbesar
    $width = strlen(decbin($n));
    
    // Header
    printf("%-{$width}s %-{$width}s %-{$width}s\n", "Decimal", "Hexadecimal", "Binary");
    
    // Loop dari 1 sampai n
    for ($i = 1; $i <= $n; $i++) {
        $decimal_str = $i;
        $hex_str = strtoupper(dechex($i));
        $binary_str = decbin($i);
        
        // Cetak tiap angka dengan padding agar rapi
        printf("%-{$width}d %-{$width}s %-{$width}s\n", $decimal_str, $hex_str, $binary_str);
    }
}

// Menjalankan fungsi
$n = (int)readline("Masukkan angka integer: ");
convert_numbers($n);

?>
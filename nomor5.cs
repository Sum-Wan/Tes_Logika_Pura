using System;

// Membuat piramid kalimat
class Program
{
    static void Main()
    {
        Console.Write("Masukkan teks: ");
        string inputText = Console.ReadLine();
        string result = DoubleStaircasePattern(inputText);
        Console.WriteLine(result);
    }

    static string DoubleStaircasePattern(string text)
    {
        // Hilangkan spasi dari teks
        text = text.Replace(" ", "");

        // Cek apakah jumlah karakter kurang dari 11
        if (text.Length < 10)
        {
            return "Mohon maaf, jumlah karakter tidak memenuhi syarat untuk membentuk pola";
        }

        string result = "";
        int index = 0;
        int col = 1;
        var rows = new System.Collections.Generic.List<string>();

        // Pola pertama (naik)
        while (index < text.Length)
        {
            string line = text.Substring(index, Math.Min(col, text.Length - index));
            rows.Add(line);
            result += line + "\n";
            index += col;
            col++;
        }

        // Pola kedua (turun dari jumlah karakter terakhir pada perulangan sebelumnya)
        col = rows[rows.Count - 1].Length;
        index = 0;

        while (index < text.Length)
        {
            string line = text.Substring(index, Math.Min(col, text.Length - index));
            result += line + "\n";
            index += col;
            col--;
        }

        return result;
    }
}
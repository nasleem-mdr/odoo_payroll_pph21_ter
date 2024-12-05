# odoo_payroll_pph21
Langkah penghitungan PPh 21 Pada aplikasi odoo
1. Buat Salary Struktur yang digunakan untuk penghitungan gaji Januari - November
   Contoh Stuktur Gaji:
   a. Name : Gaji Pokok ->  Category : Basic -> Code -> BASIC -> Condition : Always True -> Amount Type : Python (result = contract.wage)
   b. Name : Tunjangan Trans ->  Category : Allowance -> Code -> TRAV -> Condition : Always True -> Amount Type : Python (result = contract.travel_allowance)
   c. dst
   d. Buat salary rule untuk pemotongan PPh 21 berdasarkan TER (kode diambil dari pph21_v1.py)
2. Duplikat Salary Struktur diatas untuk penghitungan Gaji Bulan Desember dan Tambahkan kode Pemotongan PPh 21 (pph21_desember.py)
3. Untuk mendapatkan akumulasi/summary/aggregate penghitungan struktur gaji gunakan kode berikut:
   ```
   already_paid = sum(
   employee.mapped("slip_ids")
       .filtered(lambda s: s.date_from.year == 2024 and s.state in ("done", "paid"))
       .mapped("line_ids")
       .filtered(lambda l: l.code == "GROSS")
       .mapped("total")
    )
    result = already_paid
   ```

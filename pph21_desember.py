# Fungsi hitung PPh 21
def hitung_pph21(gaji_tahunan, status_kawin, jumlah_tanggungan, iuran_pensiun):
    # Batas maksimal tanggungan adalah 3
    if jumlah_tanggungan > 3:
        jumlah_tanggungan = 3
    
    # PTKP dasar
    ptkp = 54000000

    # Tambahan PTKP untuk status kawin
    if status_kawin == 'Married':
        ptkp += 4500000
    
    # Tambahan PTKP untuk tanggungan
    ptkp += jumlah_tanggungan * 4500000
    
    # Menghitung biaya jabatan (5% dari gaji tahunan atau maksimal 6.000.000 per tahun)
    biaya_jabatan = min(0.05 * gaji_tahunan, 6000000)
    
    # Penghasilan Kena Pajak (PKP) setelah dikurangi PTKP, biaya jabatan, dan iuran pensiun
    pkp = gaji_tahunan - ptkp - biaya_jabatan - iuran_pensiun
    if pkp <= 0:
        return 0  # Tidak ada PPh jika PKP <= 0
    
    # Menghitung PPh 21 berdasarkan PKP
    if pkp <= 50000000:
        pph21 = 0.05 * pkp
    elif pkp <= 250000000:
        pph21 = (0.05 * 50000000) + (0.15 * (pkp - 50000000))
    elif pkp <= 500000000:
        pph21 = (0.05 * 50000000) + (0.15 * 200000000) + (0.25 * (pkp - 250000000))
    else:
        pph21 = (0.05 * 50000000) + (0.15 * 200000000) + (0.25 * 250000000) + (0.30 * (pkp - 500000000))
    
    return pph21

# Contoh penggunaan (dengan asumsi data karyawan tersedia dan benar)
# Hitung gaji tahunan
gaji_tahunan = payslip.sum(GROSS, contract.date_start, contract.date_end) + GROSS
# Status kawin
status_kawin = employee.marital
# Jumlah tanggungan
jumlah_tanggungan = employee.dependent_children
# Iuran pensiun tahunan
iuran_pensiun = payslip.sum(IURAN, contract.date_start, contract.date_end) + IURAN

# Hitung PPh 21
pph21 = hitung_pph21(gaji_tahunan, status_kawin, jumlah_tanggungan, iuran_pensiun)
result = pph21

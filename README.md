# Mini_Project_2_DDP
Mini Project DDP 2 - CRUD Sistem Manajemen Absensi Mahasiswa Unmul

# FLOWCHART
<img width="2522" height="1032" alt="Flowchart_Minpro_DDP_2 drawio" src="https://github.com/user-attachments/assets/55070a49-4283-4e72-85a7-4d3bbe950436" />

# MAHASISWA
<img width="1320" height="863" alt="image" src="https://github.com/user-attachments/assets/18d566b8-437c-4124-97de-1373bfe6b886" />

Untuk user yang login sebagai mahasiswa.
Menampilkan daftar kelas/mata kuliah.
Mahasiswa memilih kelas, lalu mengisi data absensi (nama, NIM, kehadiran).
Data absensi disimpan ke list absensi.
Setelah absen, mahasiswa bisa keluar atau kembali ke menu.

# DOSEN
<img width="597" height="975" alt="image" src="https://github.com/user-attachments/assets/fbd46e2f-d2a9-4811-8d85-082d747d684d" />


Untuk user yang login sebagai dosen sesuai mata kuliah.
Untuk Dosen semua pilihan menunya sama jadi saya wakilkan dengan 1 screenshoot saja
Menu dosen terdiri dari:

<img width="421" height="264" alt="image" src="https://github.com/user-attachments/assets/f7c6c97d-0e5b-46b5-9a36-85c3b4521efd" />

1. Lihat Absen Mahasiswa
Menampilkan seluruh data absensi mahasiswa.

<img width="384" height="419" alt="image" src="https://github.com/user-attachments/assets/629b161f-6b13-4f37-84fa-cd1c32addd5d" />

2. Absenkan Mahasiswa
Dosen dapat menambah data absensi mahasiswa (nama, NIM, kehadiran).

<img width="612" height="445" alt="image" src="https://github.com/user-attachments/assets/02a2bb83-d7a6-4b49-90a7-c42914b48328" />

3. Hapus Absen Mahasiswa
Dosen dapat memilih dan menghapus data absensi tertentu berdasarkan nomor urut. Terdapat error handling jika input salah atau data kosong.

<img width="333" height="190" alt="image" src="https://github.com/user-attachments/assets/b19ca17c-8229-4db4-b878-65fdd09289da" />

4. Keluar
Keluar dari menu dosen.

<img width="505" height="165" alt="image" src="https://github.com/user-attachments/assets/82a98ca0-578c-4330-9ab9-b6e917c419c6" />

# FUNGSI LOGIN
Mengecek username dan password sesuai data di dictionary auth.
Jika benar, login berhasil; jika salah, login gagal.

<img width="591" height="250" alt="image" src="https://github.com/user-attachments/assets/e388550a-14ac-4dd4-99d9-4f6516d253fd" />

# FUNGSI MENAMPILKAN ABSEN
Menampilkan seluruh data absensi yang tersimpan di list absensi.
Menampilkan data dengan nomor urut agar mudah dipilih saat penghapusan.

<img width="347" height="151" alt="image" src="https://github.com/user-attachments/assets/b5d73075-f90c-4cbf-bb02-27bdaf125783" />

# FUNGSI LOGOUT DAN KELUAR
Menampilkan pesan logout atau keluar, lalu mengakhiri program.

<img width="399" height="249" alt="image" src="https://github.com/user-attachments/assets/4f3030d1-a259-4022-bfae-ac96370ef460" />

# FUNGSI AKHIR
Menanyakan apakah user ingin keluar atau kembali ke menu utama.

<img width="576" height="730" alt="image" src="https://github.com/user-attachments/assets/db1259a5-ef41-4fb6-a2e7-4fb251fee993" />

# FUNGSI KERJA
Fungsi utama yang menangani proses login.
Setelah login, user diarahkan ke menu sesuai role (mahasiswa atau dosen).

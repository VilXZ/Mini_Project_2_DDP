absensi = []

auth = {"dosenddp":"dosenddplogin",
        "dosenpti":"dosenptilogin",
        "dosenbing":"dosenbinglogin",
        "dosenksi":"dosenksilogin",
        "dosenmatdis":"dosenmatdislogin",
        "dosenpp":"dosenpplogin",
        "dosenagama":"dosenagamalogin",
        "mahasiswa":"mahasiswalogin"}

def login(usn, pw):
        while True:
            if usn in auth and auth[usn] == pw:
                return True
            else:
                return False
            
def logout():
    print("Anda telah logout")

def keluar():
    print("\nAnda Keluar")
    exit()

def akhir():
    pilih_akhir = input("Keluar? (y/n)")
    if pilih_akhir == "y":
        print("\nKetemu Lagi Nanti!")
        return keluar()
    elif pilih_akhir == "n":
        return kerja()
    else:
        print("Input Tidak Valid")
        return akhir()

def mahasiswa():
    print("\nAnda Masuk!")
    print("\n==== Kelas ====")
    print("\n1. Dasar - Dasar Pemrograman")
    print("2. Pengantar Teknologi Informasi")
    print("3. Bahasa Inggris")
    print("4. Konsep Sistem Informasi")
    print("5. Matematika Diskrit")
    print("6. Pendidikan Pancasila")
    print("7. Pendidikan Agama")
    print("8. logout")
    pilih_kelas = input("\nPilih Kelas untuk Absen : ")
    if pilih_kelas == "1":
        print("\nMasukkan Data Anda")
        nama = input("\nMasukkan Nama = ")
        nim = input("Masukkan NIM = ")
        kehadiran = input("(Hadir/Sakit/Izin/Alpa) = ")
        data_absensi = (nama, nim, kehadiran)
        absensi.append(data_absensi)
        a = absensi[-1]
        print("\n| Data Kehadiran ",)
        print("| Nama      :", a[0])
        print("| NIM       :", a[1])
        print("| Kehadiran :", a[2])
        print("\nAbsen Anda telah direkam")
        print("--------------------------")
        akhir()
    elif pilih_kelas == "2":
        print("\nMasukkan Data Anda")
        nama = input("\nMasukkan Nama = ")
        nim = input("Masukkan NIM = ")
        kehadiran = input("(Hadir/Sakit/Izin/Alpa) = ")
        data_absensi = (nama, nim, kehadiran)
        absensi.append(data_absensi)
        a = absensi[-1]
        print("\n| Data Kehadiran ",)
        print("| Nama      :", a[0])
        print("| NIM       :", a[1])
        print("| Kehadiran :", a[2])
        print("\nAbsen Anda telah direkam")
        print("--------------------------")
        akhir()
    elif pilih_kelas == "3":
        print("\nMasukkan Data Anda")
        nama = input("\nMasukkan Nama = ")
        nim = input("Masukkan NIM = ")
        kehadiran = input("(Hadir/Sakit/Izin/Alpa) = ")
        data_absensi = (nama, nim, kehadiran)
        absensi.append(data_absensi)
        a = absensi[-1]
        print("\n| Data Kehadiran ",)
        print("| Nama      :", a[0])
        print("| NIM       :", a[1])
        print("| Kehadiran :", a[2])
        print("\nAbsen Anda telah direkam")
        print("--------------------------")
        akhir()
    elif pilih_kelas == "4":
        print("\nMasukkan Data Anda")
        nama = input("\nMasukkan Nama = ")
        nim = input("Masukkan NIM = ")
        kehadiran = input("(Hadir/Sakit/Izin/Alpa) = ")
        data_absensi = (nama, nim, kehadiran)
        absensi.append(data_absensi)
        a = absensi[-1]
        print("\n| Data Kehadiran ",)
        print("| Nama      :", a[0])
        print("| NIM       :", a[1])
        print("| Kehadiran :", a[2])
        print("\nAbsen Anda telah direkam")
        print("--------------------------")
        akhir()
    elif pilih_kelas == "5":
        print("\nMasukkan Data Anda")
        nama = input("\nMasukkan Nama = ")
        nim = input("Masukkan NIM = ")
        kehadiran = input("(Hadir/Sakit/Izin/Alpa) = ")
        data_absensi = (nama, nim, kehadiran)
        absensi.append(data_absensi)
        a = absensi[-1]
        print("\n| Data Kehadiran ",)
        print("| Nama      :", a[0])
        print("| NIM       :", a[1])
        print("| Kehadiran :", a[2])
        print("\nAbsen Anda telah direkam")
        print("--------------------------")
        akhir()
    elif pilih_kelas == "6":
        print("\nMasukkan Data Anda")
        nama = input("\nMasukkan Nama = ")
        nim = input("Masukkan NIM = ")
        kehadiran = input("(Hadir/Sakit/Izin/Alpa) = ")
        data_absensi = (nama, nim, kehadiran)
        absensi.append(data_absensi)
        a = absensi[-1]
        print("\n| Data Kehadiran ",)
        print("| Nama      :", a[0])
        print("| NIM       :", a[1])
        print("| Kehadiran :", a[2])
        print("\nAbsen Anda telah direkam")
        print("--------------------------")
        akhir()
    elif pilih_kelas == "7":
        print("\nMasukkan Data Anda")
        nama = input("\nMasukkan Nama = ")
        nim = input("Masukkan NIM = ")
        kehadiran = input("(Hadir/Sakit/Izin/Alpa) = ")
        data_absensi = (nama, nim, kehadiran)
        absensi.append(data_absensi)
        a = absensi[-1]
        print("\n| Data Kehadiran ",)
        print("| Nama      :", a[0])
        print("| NIM       :", a[1])
        print("| Kehadiran :", a[2])
        print("\nAbsen Anda telah direkam")
        print("--------------------------")
        akhir()
    elif pilih_kelas == "8":
        logout()

def tampilkan_absensi():
    if not absensi:
        print("\nBelum ada data absen.")
    else:
        for idx, a in enumerate(absensi):
            print(f"\n| Data Kehadiran Pertemuan {idx+1}")
            print("| Nama      :", a[0])
            print("| NIM       :", a[1])
            print("| Kehadiran :", a[2])
            print("--------------------------")

def dosenddp():
    while True:
        print("1. Lihat Absen Mahasiswa")
        print("2. Absenkan Mahasiswa")
        print("3. Hapus Absen Mahasiswa")
        print("4. Keluar")

        ddppilih = input("Pilihan : ")
        
        if ddppilih == "1":
            tampilkan_absensi()
        elif ddppilih == "2":
            print("\nMasukkan Data Mahasiswa")
            nama = input("\nMasukkan Nama = ")
            nim = input("Masukkan NIM = ")
            kehadiran = input("(Hadir/Sakit/Izin/Alpa) = ")
            data_absensi = (nama, nim, kehadiran)
            absensi.append(data_absensi)
            a = absensi[-1]
            print("\n| Data Kehadiran ")
            print("| Nama      :", a[0])
            print("| NIM       :", a[1])
            print("| Kehadiran :", a[2])
            print("\nAbsen Mahasiswa telah direkam")
            print("--------------------------")
        elif ddppilih == "3":
            if not absensi:
                print("Tidak ada data absen untuk dihapus.")
            else:
                tampilkan_absensi()
                try:
                    idx = int(input("Masukkan nomor absen yang ingin dihapus: ")) - 1
                    if 0 <= idx < len(absensi):
                        hapus = absensi.pop(idx)
                        print(f"Absen mahasiswa '{hapus[0]}' berhasil dihapus.")
                    else:
                        print("Nomor absen tidak valid.")
                except ValueError:
                    print("Input harus berupa angka.")
            print("--------------------------")
        elif ddppilih == "4":
            print("Keluar")
            break

def dosenpti():
    while True:
        print("1. Lihat Absen Mahasiswa")
        print("2. Absenkan Mahasiswa")
        print("3. Hapus Absen Mahasiswa")
        print("4. Keluar")

        ptipilih = input("Pilihan : ")
        
        if ptipilih == "1":
            tampilkan_absensi()
        elif ptipilih == "2":
            print("\nMasukkan Data Mahasiswa")
            nama = input("\nMasukkan Nama = ")
            nim = input("Masukkan NIM = ")
            kehadiran = input("(Hadir/Sakit/Izin/Alpa) = ")
            data_absensi = (nama, nim, kehadiran)
            absensi.append(data_absensi)
            a = absensi[-1]
            print("\n| Data Kehadiran ",)
            print("| Nama      :", a[0])
            print("| NIM       :", a[1])
            print("| Kehadiran :", a[2])
            print("\nAbsen Mahasiswa telah direkam")
            print("--------------------------")
        elif ptipilih == "3":
            if not absensi:
                print("Tidak ada data absen untuk dihapus.")
            else:
                tampilkan_absensi()
                try:
                    idx = int(input("Masukkan nomor absen yang ingin dihapus: ")) - 1
                    if 0 <= idx < len(absensi):
                        hapus = absensi.pop(idx)
                        print(f"Absen mahasiswa '{hapus[0]}' berhasil dihapus.")
                    else:
                        print("Nomor absen tidak valid.")
                except ValueError:
                    print("Input harus berupa angka.")
            print("--------------------------")
        elif ptipilih == "4":
            print("\nKeluar")
            break

def dosenbing():
    while True:
        print("1. Lihat Absen Mahasiswa")
        print("2. Absenkan Mahasiswa")
        print("3. Hapus Absen Mahasiswa")
        print("4. Keluar")

        bingpilih = input("Pilihan : ")
        
        if bingpilih == "1":
            tampilkan_absensi()
        elif bingpilih == "2":
            print("\nMasukkan Data Mahasiswa")
            nama = input("\nMasukkan Nama = ")
            nim = input("Masukkan NIM = ")
            kehadiran = input("(Hadir/Sakit/Izin/Alpa) = ")
            data_absensi = (nama, nim, kehadiran)
            absensi.append(data_absensi)
            a = absensi[-1]
            print("\n| Data Kehadiran ",)
            print("| Nama      :", a[0])
            print("| NIM       :", a[1])
            print("| Kehadiran :", a[2])
            print("\nAbsen Mahasiswa telah direkam")
            print("--------------------------")
        elif bingpilih == "3":
            if not absensi:
                print("Tidak ada data absen untuk dihapus.")
            else:
                tampilkan_absensi()
                try:
                    idx = int(input("Masukkan nomor absen yang ingin dihapus: ")) - 1
                    if 0 <= idx < len(absensi):
                        hapus = absensi.pop(idx)
                        print(f"Absen mahasiswa '{hapus[0]}' berhasil dihapus.")
                    else:
                        print("Nomor absen tidak valid.")
                except ValueError:
                    print("Input harus berupa angka.")
            print("--------------------------")
        elif bingpilih == "4":
            print("\nKeluar")
            break

def dosenksi():
    while True:
        print("1. Lihat Absen Mahasiswa")
        print("2. Absenkan Mahasiswa")
        print("3. Hapus Absen Mahasiswa")
        print("4. Keluar")

        ksipilih = input("Pilihan : ")
        
        if ksipilih == "1":
            tampilkan_absensi()
        elif ksipilih == "2":
            print("\nMasukkan Data Mahasiswa")
            nama = input("\nMasukkan Nama = ")
            nim = input("Masukkan NIM = ")
            kehadiran = input("(Hadir/Sakit/Izin/Alpa) = ")
            data_absensi = (nama, nim, kehadiran)
            absensi.append(data_absensi)
            a = absensi[-1]
            print("\n| Data Kehadiran ",)
            print("| Nama      :", a[0])
            print("| NIM       :", a[1])
            print("| Kehadiran :", a[2])
            print("\nAbsen Mahasiswa telah direkam")
            print("--------------------------")
        elif ksipilih == "3":
            if not absensi:
                print("Tidak ada data absen untuk dihapus.")
            else:
                tampilkan_absensi()
                try:
                    idx = int(input("Masukkan nomor absen yang ingin dihapus: ")) - 1
                    if 0 <= idx < len(absensi):
                        hapus = absensi.pop(idx)
                        print(f"Absen mahasiswa '{hapus[0]}' berhasil dihapus.")
                    else:
                        print("Nomor absen tidak valid.")
                except ValueError:
                    print("Input harus berupa angka.")
            print("--------------------------")
        elif ksipilih == "4":
            print("\nKeluar")
            break

def dosenmatdis():
    while True:
        print("1. Lihat Absen Mahasiswa")
        print("2. Absenkan Mahasiswa")
        print("3. Hapus Absen Mahasiswa")
        print("4. Keluar")

        matdispilih = input("Pilihan : ")
        
        if matdispilih == "1":
            tampilkan_absensi()
        elif matdispilih == "2":
            print("\nMasukkan Data Mahasiswa")
            nama = input("\nMasukkan Nama = ")
            nim = input("Masukkan NIM = ")
            kehadiran = input("(Hadir/Sakit/Izin/Alpa) = ")
            data_absensi = (nama, nim, kehadiran)
            absensi.append(data_absensi)
            a = absensi[-1]
            print("\n| Data Kehadiran ",)
            print("| Nama      :", a[0])
            print("| NIM       :", a[1])
            print("| Kehadiran :", a[2])
            print("\nAbsen Mahasiswa telah direkam")
            print("--------------------------")
        elif matdispilih == "3":
            if not absensi:
                print("Tidak ada data absen untuk dihapus.")
            else:
                tampilkan_absensi()
                try:
                    idx = int(input("Masukkan nomor absen yang ingin dihapus: ")) - 1
                    if 0 <= idx < len(absensi):
                        hapus = absensi.pop(idx)
                        print(f"Absen mahasiswa '{hapus[0]}' berhasil dihapus.")
                    else:
                        print("Nomor absen tidak valid.")
                except ValueError:
                    print("Input harus berupa angka.")
            print("--------------------------")
        elif matdispilih == "4":
            print("Keluar")
            break

def dosenpp():
    while True:
        print("1. Lihat Absen Mahasiswa")
        print("2. Absenkan Mahasiswa")
        print("3. Hapus Absen Mahasiswa")
        print("4. Keluar")

        pppilih = input("Pilihan : ")
        
        if pppilih == "1":
            tampilkan_absensi()
        elif pppilih == "2":
            print("\nMasukkan Data Mahasiswa")
            nama = input("\nMasukkan Nama = ")
            nim = input("Masukkan NIM = ")
            kehadiran = input("(Hadir/Sakit/Izin/Alpa) = ")
            data_absensi = (nama, nim, kehadiran)
            absensi.append(data_absensi)
            a = absensi[-1]
            print("\n| Data Kehadiran ",)
            print("| Nama      :", a[0])
            print("| NIM       :", a[1])
            print("| Kehadiran :", a[2])
            print("\nAbsen Mahasiswa telah direkam")
            print("--------------------------")
        elif pppilih == "3":
            if not absensi:
                print("Tidak ada data absen untuk dihapus.")
            else:
                tampilkan_absensi()
                try:
                    idx = int(input("Masukkan nomor absen yang ingin dihapus: ")) - 1
                    if 0 <= idx < len(absensi):
                        hapus = absensi.pop(idx)
                        print(f"Absen mahasiswa '{hapus[0]}' berhasil dihapus.")
                    else:
                        print("Nomor absen tidak valid.")
                except ValueError:
                    print("Input harus berupa angka.")
            print("--------------------------")
        elif pppilih == "4":
            print("\nKeluar")
            break

def dosenagama():
    while True:
        print("1. Lihat Absen Mahasiswa")
        print("2. Absenkan Mahasiswa")
        print("3. Hapus Absen Mahasiswa")
        print("4. Keluar")

        agamapilih = input("Pilihan : ")
        
        if agamapilih == "1":
            tampilkan_absensi()
        elif agamapilih == "2":
            print("\nMasukkan Data Mahasiswa")
            nama = input("\nMasukkan Nama = ")
            nim = input("Masukkan NIM = ")
            kehadiran = input("(Hadir/Sakit/Izin/Alpa) = ")
            data_absensi = (nama, nim, kehadiran)
            absensi.append(data_absensi)
            a = absensi[-1]
            print("\n| Data Kehadiran ",)
            print("| Nama      :", a[0])
            print("| NIM       :", a[1])
            print("| Kehadiran :", a[2])
            print("\nAbsen Mahasiswa telah direkam")
            print("--------------------------")
        elif agamapilih == "3":
            if not absensi:
                print("Tidak ada data absen untuk dihapus.")
            else:
                tampilkan_absensi()
                try:
                    idx = int(input("Masukkan nomor absen yang ingin dihapus: ")) - 1
                    if 0 <= idx < len(absensi):
                        hapus = absensi.pop(idx)
                        print(f"Absen mahasiswa '{hapus[0]}' berhasil dihapus.")
                    else:
                        print("Nomor absen tidak valid.")
                except ValueError:
                    print("Input harus berupa angka.")
            print("--------------------------")
        elif agamapilih == "4":
            print("\nKeluar")
            break

def kerja():
    while True:
        usn = input("\nMasukkan username akun : ")
        pw = input("\nMasukkan password akun : ") 
        
        if login(usn, pw):
            print("\nLogin Berhasil")
            if usn == "mahasiswa":
                mahasiswa()
            elif usn == "dosenddp":
                dosenddp()
            elif usn == "dosenpti":
                dosenpti()
            elif usn == "dosenbing":
                dosenbing()
            elif usn == "dosenksi":
                dosenksi()
            elif usn == "dosenmatdis":
                dosenmatdis()
            elif usn == "dosenpp":
                dosenpp()
            elif usn == "dosenagama":
                dosenagama()
            else:
                print("Gagal Masuk!")
        else:
            print("Login Gagal")
            break

kerja()
'''=================================================================================================================================='''
'''                                                 SISTEM TOKO BOUKET BUNGA                                                         '''
'''=================================================================================================================================='''

import json
import os
import time
import pwinput
from prettytable import PrettyTable

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')
    
'''=================================================================================================================================='''
'''                                                      JSON                                                                        '''
'''=================================================================================================================================='''

def muat_users():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("[!] File users.json tidak ditemukan.")
        return []
    
def simpan_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)
        
def muat_bunga():
    try:
        with open('bunga.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("[!] File bunga.json tidak ditemukan.")
        return []
    
def simpan_bunga(data):
    with open('bunga.json', 'w') as file:
        json.dump(data, file, indent=4)
        
def muat_pesanan():
    try:
        with open('pesanan.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("[!] File pesanan.json tidak ditemukan.")
        return []
    
def simpan_pesanan(data):
    with open('pesanan.json', 'w') as file:
        json.dump(data, file, indent=4)
        
'''=================================================================================================================================='''
'''                                                         REGISTRASI                                                                '''
'''=================================================================================================================================='''

def daftar():
    bersihkan_layar()
    print("┌──────────────────────────────────┐")
    print("│       🌷REGISTRASI AKUN🌷        │")
    print("└──────────────────────────────────┘")

    users = muat_users()
    percobaan = 0
    
    while percobaan < 3:
        username_baru = input("- Masukkan username (5-20 Huruf,tanpa angka): ")
        
        if not username_baru.isalpha():
             print("[!] Username hanya boleh berisi huruf. <<")
             percobaan += 1
             time.sleep(1)
        elif not (5 <= len(username_baru) <= 20):
             print("[!] Panjang username harus antara 5 hingga 20 karakter. <<")
             percobaan += 1
             time.sleep(1)
        elif any(pengguna['username'] == username_baru for pengguna in users):
            print("[!] Username tidak tersedia. Silakan pilih username lain. <<")
            time.sleep(1)
        else:
            while percobaan < 3:
                password_baru = pwinput.pwinput("- Masukkan password (min 8 hingga 15 karakter): ")
                
                if not (5 <= len(password_baru) <= 15):
                    print("[!] Password harus memiliki minimal 8 hingga 15 karakter. <<")
                    percobaan += 1
                    time.sleep(1)
                else:
                    pengguna_baru = {
                        "username": username_baru,
                        "password": password_baru,
                        "saldo": 0,
                        "pembelian_selesai": 0,
                        "voucher": False
                    }
                    users.append(pengguna_baru)
                    simpan_users(users)
                    print("\n[✓] Registrasi berhasil🌷")
                    time.sleep(3)
                    return

'''=================================================================================================================================='''
'''                                                             LOGIN                                                                 '''
'''=================================================================================================================================='''

def login_user():
    bersihkan_layar()
    users = muat_users()
    percobaan = 0
    
    while percobaan < 3:
        print("┌──────────────────────────────────┐")
        print("│          🌷LOGIN USER🌷         │")
        print("└──────────────────────────────────┘")
        username = input("- Masukkan username: ")
        password = pwinput.pwinput("- Masukkan password: ")

        user_ditemukan = False
        for pengguna in users:
            if pengguna['username'] == username and pengguna['password'] == password:
                print("\n[✓] Login berhasil🌷")
                time.sleep(2)
                return pengguna
        percobaan += 1 

        if percobaan < 3: 
            bersihkan_layar()
            print(f"[!] Username atau password salah. Sisa percobaan: {3 - percobaan}🥀")

    print("\n[!] Anda telah salah memasukkan password sebanyak 3 kali🥀")
    print("Harap tunggu 6 detik untuk mencoba lagi.")
    time.sleep(6)
    return None 

def login_admin():
    bersihkan_layar()
    admins = {
        "aya": "admin123",
        "ibrah": "admin123",
        "carla": "admin123"
    }
    
    percobaan = 0
    while percobaan < 3:
        print("┌──────────────────────────────────┐")
        print("│          🌼LOGIN ADMIN🌼        │")
        print("└──────────────────────────────────┘")
        username = input("- Masukkan username: ")
        password = pwinput.pwinput("- Masukkan password: ")

        if username in admins and admins[username] == password:
            print("\n[✓] Login berhasil🌷")
            time.sleep(2)
            return username
        else:
            percobaan += 1 
            if percobaan < 3: 
                bersihkan_layar()
                print(f"[!] Username atau password salah. Sisa percobaan: {3 - percobaan}🥀")
                
    print("\n[!] Anda telah salah memasukkan password sebanyak 3 kali🥀")
    print("Harap tunggu 60 detik untuk mencoba lagi.")
    time.sleep(6) 
    return None

'''=================================================================================================================================='''
'''                                                         TOP UP SALDO                                                              '''
'''=================================================================================================================================='''

def topup(user):
    bersihkan_layar()
    print(f"Saldo Anda Saat Ini: Rp {user['saldo']:,}")
    print("\n--- Pilih Nominal Top Up ---")
    print("┌──────────────────────────────────┐")
    print("│         ⚘ NOMINAL TOP UP ⚘       │")
    print("├──────────────────────────────────┤")
    print("│ 1. Rp 50,000                     │")
    print("│ 2. Rp 80,000                     │") 
    print("│ 3. Rp 100,000                    │")
    print("│ 4. Rp 200,000                    │")
    print("│ 5. Rp 500,000                    │")
    print("│ 6. Kembali                       │")
    print("└──────────────────────────────────┘")
    pilihan_nominal = input("Pilih nominal top up: ")

    jumlah_topup = 0
    nominal_pilihan = "" 

    if pilihan_nominal == '1':
        jumlah_topup = 50000
        nominal_pilihan = "Rp 50,000"
    elif pilihan_nominal == '2':
        jumlah_topup = 80000
        nominal_pilihan = "Rp 80,000"
    elif pilihan_nominal == '3':
        jumlah_topup = 100000
        nominal_pilihan = "Rp 100,000"
    elif pilihan_nominal == '4':
        jumlah_topup = 200000
        nominal_pilihan = "Rp 200,000"
    elif pilihan_nominal == '5':
        jumlah_topup = 500000
        nominal_pilihan = "Rp 500,000"
    elif pilihan_nominal == '6':
        return # Kembali
    else:
        print("[!] Pilihan nominal tidak valid.")
        time.sleep(2)
        return

    if jumlah_topup > 0:
        bersihkan_layar()
        print("--- PEMBAYARAN TOP UP ---")
        print(f"Anda memilih Top Up: {nominal_pilihan}")
        print("\nMemverifikasi pembayaran...")
        time.sleep(3) 

        percobaan_pass = 0
        verifikasi_berhasil = False
        while percobaan_pass < 3:
            print("\n--- Verifikasi Keamanan ---")
            password_verifikasi = pwinput.pwinput(prompt="Masukkan password Anda lagi untuk konfirmasi: ")
            
            if password_verifikasi == user['password']:
                verifikasi_berhasil = True
                print("[✓] Verifikasi berhasil.")
                break
            else:
                percobaan_pass += 1
                print(f"[!] Password salah. Sisa percobaan: {3 - percobaan_pass}")

        if not verifikasi_berhasil:
            print("\n[!] Anda telah salah memasukkan password sebanyak 3 kali.")
            print("Proses top up dibatalkan. Harap tunggu 6 detik.")
            time.sleep(6)
            return 

        if verifikasi_berhasil:
            daftar_pengguna = muat_users()
            for user in daftar_pengguna:
                if user['username'] == user['username']:
                    user['saldo'] += jumlah_topup
                    saldo_baru = user['saldo']
                    break
            simpan_users(daftar_pengguna)
            print(f"\n[✓] Top up sebesar Rp {jumlah_topup:,} berhasil!")
            print(f"[i] Saldo baru Anda: Rp {saldo_baru:,}")
            time.sleep(3)

'''=================================================================================================================================='''
'''                                                         FUNGSI BUNGA                                                             '''
'''=================================================================================================================================='''

def tambah_bunga():
    bersihkan_layar()
    print("┌──────────────────────────────────┐")
    print("│        🌼 TAMBAH BUKET 🌼       │")
    print("└──────────────────────────────────┘")

    daftar_bunga = muat_bunga()
    
    while True:
        nama_bunga = input("- Masukkan nama buket bunga: ")
        if not nama_bunga.strip():
            print("[!] Nama buket tidak boleh kosong. Coba lagi.🥀")
        elif not nama_bunga.replace(" ", "").isalpha():
            print("[!] Nama buket hanya boleh berisi huruf. Coba lagi.🥀")
        else:
            break
        
    while True:
        try:
            harga_bunga = int(input("- Masukkan harga buket bunga (Rp 70.000 - 1.000.000): "))
            if not (70000 <= harga_bunga <= 1000000):
                print("[!] Harga harus di antara Rp 70.000 dan Rp 1.000.000. Coba lagi.🥀")
            else:
                break
        except ValueError or KeyboardInterrupt:
            print("[!] Harga harus berupa angka. Silakan coba lagi.")
            
    while True:
        try:
            stok_bunga = int(input("- Masukkan stok buket bunga (1 - 20): "))
            if not (1 <= stok_bunga <= 20):
                print("[!] Stok harus di antara 1 dan 20. Coba lagi.🥀")
            else:
                break
        except ValueError or KeyboardInterrupt:
            print("[!] Stok harus berupa angka. Silakan coba lagi.")
            
    if not daftar_bunga:
        id_baru = 1
    else:
        id_terakhir = int(daftar_bunga[-1]['id'])
        id_baru = id_terakhir + 1
        
    bunga_baru = {
        "id": str(id_baru),
        "nama": nama_bunga,
        "harga": harga_bunga,
        "stok": stok_bunga
    }
    
    bersihkan_layar()
    daftar_bunga.append(bunga_baru)
    simpan_bunga(daftar_bunga)
    print("DETAIL BUKET 🌼:")
    print(f"- ID Buket: {bunga_baru['id']}")
    print(f"- Nama Buket: {bunga_baru['nama']}")
    print(f"- Harga Buket: Rp {bunga_baru['harga']:,}")
    print(f"- Stok Buket: {bunga_baru['stok']}")
    
    print("\n[✓] Bunga berhasil ditambahkan🌷")
    input("\ntekan Enter untuk kembali...")

def ubah_bunga():
    bersihkan_layar()
    print("┌──────────────────────────────────┐")
    print("│ 	    🌼 UPDATE BUKET 🌼 	  │")
    print("└──────────────────────────────────┘")

    daftar_bunga = muat_bunga()
    if not daftar_bunga:
        print("\n>> Katalog bunga kosong. <<")
        input("\ntekan Enter untuk kembali...")
        return
    
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama Buket", "Harga (Rp)", "Stok"]
    tabel.align["Nama Buket"] = "l"
    tabel.align["Harga (Rp)"] = "r"
    for bunga in daftar_bunga:
        harga_format = f"{bunga['harga']:,}"
        tabel.add_row([bunga['id'], bunga['nama'], harga_format, bunga['stok']])
    print(tabel)
    
    id_bunga = input("\n- Masukkan ID buket yang ingin diupdate: ")
    bunga_ditemukan = False

    
    for bunga in daftar_bunga:
        if bunga['id'] == id_bunga:
            bunga_ditemukan = True
            print(f"\n- Buket yang dipilih: {bunga['nama']} (ID: {bunga['id']})")
            
            while True:
                nama_baru_str = input(f"- Masukkan nama buket baru (Enter untuk skip): ")
                if not nama_baru_str.strip():
                    nama_baru = bunga['nama'] 
                    break
                elif not nama_baru_str.replace(" ", "").isalpha():
                    print("[!] Nama buket hanya boleh berisi huruf. Coba lagi.🥀")
                else:
                    nama_baru = nama_baru_str 
                    break 	
            
            while True:
                harga_baru_str = input(f"- Masukkan harga baru (Enter untuk skip): ")
                if not harga_baru_str.strip():
                    harga_baru = bunga['harga'] 
                    break
                
                try:
                    harga_baru_int = int(harga_baru_str)
                    if not (70000 <= harga_baru_int <= 1000000):
                        print("[!] Harga harus di antara Rp 70.000 dan Rp 1.000.000. Coba lagi.🥀")
                    else:
                        harga_baru = harga_baru_int 
                        break
                except ValueError:
                    print("[!] Harga harus berupa angka. Silakan coba lagi.")
                    
            while True:
                stok_baru_str = input(f"- Masukkan stok baru (Enter untuk skip): ")
                if not stok_baru_str.strip():
                    stok_baru = bunga['stok'] 
                    break
                    
                try:
                    stok_baru_int = int(stok_baru_str)
                    if not (1 <= stok_baru_int <= 20):
                        print("[!] Stok harus di antara 1 dan 20. Coba lagi.🥀")
                    else:
                        stok_baru = stok_baru_int
                        break
                except ValueError:
                    print("[!] Stok harus berupa angka. Silakan coba lagi.")
            
            bunga['nama'] = nama_baru
            bunga['harga'] = harga_baru
            bunga['stok'] = stok_baru
            
            simpan_bunga(daftar_bunga)
            print("\nDETAIL BUKET YANG DIUPDATE 🌼")
            print(f"- Nama Buket: {bunga['nama']}")
            print(f"- Harga Buket: Rp {bunga['harga']:,}")
            print(f"- Stok Buket: {bunga['stok']}")
            
            print("\n[✓] Bunga berhasil diupdate🌷")
            input("\ntekan Enter untuk kembali...")
            break 
    
    if not bunga_ditemukan:
        print(f"\n[!] Buket tidak ditemukan.🥀")
        input("\ntekan Enter untuk kembali...")

def hapus_bunga():
    bersihkan_layar()
    print("┌──────────────────────────────────┐")
    print("│        🌼 HAPUS BUKET 🌼        │")
    print("└──────────────────────────────────┘")

    daftar_bunga = muat_bunga()
    
    if not daftar_bunga:
        print("\n>> Katalog bunga kosong. <<")
        input("\ntekan Enter untuk kembali...")
        return
    
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama Buket", "Harga (Rp)", "Stok"]
    for bunga in daftar_bunga:
        harga_format = f"{bunga['harga']:,}"
        tabel.add_row([bunga['id'], bunga['nama'], harga_format, bunga['stok']])
    print(tabel)

    idhapus = input("\n- Masukkan ID buket yang ingin dihapus: ")
    
    ditemukan = False
    bungadihapus = None 

    for bunga in daftar_bunga:
        if bunga['id'] == idhapus:
            ditemukan = True 
            bungadihapus = bunga 
            break 
            
    if ditemukan == True:
        daftar_bunga.remove(bungadihapus)
        simpan_bunga(daftar_bunga) 
        print(f"\n[✓] Buket '{bungadihapus['nama']}' berhasil dihapus.")
    else:
        print(f"\n[!] ID Bunga tidak ditemukan.")
    
    input("\ntekan Enter untuk kembali...")

'''=================================================================================================================================='''
'''                                                   PESANAN BUKET TEMPLATE                                                         '''
'''=================================================================================================================================='''

def pesan_buket_template(data_pengguna):
    bersihkan_layar()
    print("--- PESAN BUKET TEMPLATE ---")
    data_bunga = muat_bunga()
    
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama Buket", "Harga (Rp)", "Stok"]
    for item in data_bunga:
        tabel.add_row([item['id'], item['nama'], f"{item['harga']:,}", item['stok']])
    print(tabel)

    id_pilihan = input("Masukkan ID Buket yang ingin dipesan: ")

    item_dipilih = next((item for item in data_bunga if item['id'] == id_pilihan), None)

    if item_dipilih:
        if item_dipilih['stok'] <= 0:
            print("\n[!] Maaf, stok untuk item ini habis.")
            time.sleep(2)
            return

        harga_asli = item_dipilih['harga'] 
        harga_final = harga_asli 		
        voucher_digunakan = False

        if data_pengguna.get('punya_voucher', False):
            konfirmasi_voucher = input(f"\n[🎉] Anda memiliki voucher 50%! Harga asli Rp {harga_asli:,}. Gunakan? (y/n): ").lower()
            if konfirmasi_voucher == 'y':
                harga_final = int(harga_asli * 0.5) 
                voucher_digunakan = True
                print(f"[🎉] Harga setelah diskon: Rp {harga_final:,}")
        
        if data_pengguna['saldo'] <= 0:
            print("\n[!] Saldo Anda Rp 0. Pembelian dihentikan. Silakan Top Up.")
            time.sleep(2)
            return
            
        if data_pengguna['saldo'] < harga_final:
            print(f"\n[!] Saldo Anda (Rp {data_pengguna['saldo']:,}) tidak mencukupi untuk pesanan (Rp {harga_final:,}).")
            time.sleep(2)
            return
            
        konfirmasi_pesan = input(f"Konfirmasi pembelian '{item_dipilih['nama']}' seharga Rp {harga_final:,}? (y/n): ").lower()

        if konfirmasi_pesan == 'y':
            semua_pesanan = muat_pesanan()
            
            id_pesanan_baru = len(semua_pesanan) + 1 
            pesanan_baru = {
                "id": id_pesanan_baru, 
                "username": data_pengguna['username'],
                "jenis": "template",
                "item": item_dipilih, 
                "total_harga": harga_final, 
                "status": "pending", 
                "voucher_digunakan": voucher_digunakan,
                "stok_dikurangi": False 
            }
            semua_pesanan.append(pesanan_baru)
            simpan_pesanan(semua_pesanan)
            
            daftar_pengguna_update = muat_users()
            saldo_user_terbaru = 0 
            for user in daftar_pengguna_update:
                if user['username'] == data_pengguna['username']:
                    user['saldo'] -= harga_final
                    saldo_user_terbaru = user['saldo'] 
                    if voucher_digunakan:
                        user['punya_voucher'] = False
                    break
            simpan_users(daftar_pengguna_update)
            
            daftar_bunga_update = muat_bunga()
            for bunga in daftar_bunga_update:
                if bunga['id'] == item_dipilih['id']: 
                    bunga['stok'] -= 1
                    break
            simpan_bunga(daftar_bunga_update)
            
            print("\n[✓] Pembelian berhasil! Pesanan sedang diproses.")
            print("\n--- STRUK ---")
            print(f"ID Pesanan : {pesanan_baru['id']}")
            print(f"Item 	 	 : {item_dipilih['nama']}")
            if voucher_digunakan:
                print(f"Harga Asli : Rp {harga_asli:,}")
                print("Diskon 	 : 50%")
            print(f"Total Bayar: Rp {harga_final:,}")
            print(f"Sisa Saldo : Rp {saldo_user_terbaru:,}") 
            input("\nTekan Enter untuk kembali...")

        else:
            print("\nPembelian dibatalkan.")
            time.sleep(2)
    else:
        print("\n[!] ID tidak valid.")
        time.sleep(2)
'''=================================================================================================================================='''
'''                                                       PESANAN BUKET KUSTOM                                                      '''
'''=================================================================================================================================='''

def pesan_buket_kustom(data_pengguna):
    bersihkan_layar()
    print("--- PESAN BUKET KUSTOM ---")

    harga_dasar = 75000
    harga_asli = 30000
    harga_ukuran = {"1": ("Kecil", 20000), "2": ("Sedang", 40000), "3": ("Besar", 60000)}
    biaya_uang = 50000

    print("\nPilih jenis bunga:")
    print("1. Bunga Asli (+Rp 30,000)")
    print("2. Bunga Palsu (+Rp 0)")
    pilih_asli = input("Pilih (1/2): ")
    bunga_asli = (pilih_asli == "1")

    print("\nPilih jenis bunga utama:")
    daftar_bunga = ["Mawar", "Lily", "Tulip", "Melati", "Anggrek"]
    for i, b in enumerate(daftar_bunga, 1):
        print(f"{i}. {b}")
    pilih_bunga = input("Pilih (1-5): ")
    bunga_utama = daftar_bunga[int(pilih_bunga)-1] if pilih_bunga in map(str, range(1,6)) else "Mawar"

    print("\nPilih warna dominan:")
    warna_opsi = ["Merah", "Putih", "Pink", "Ungu", "Kuning"]
    for i, w in enumerate(warna_opsi, 1):
        print(f"{i}. {w}")
    pilih_warna = input("Pilih (1-5): ")
    warna = warna_opsi[int(pilih_warna)-1] if pilih_warna in map(str, range(1,6)) else "Merah"

    print("\nPilih ukuran buket:")
    for k, (nama, harga) in harga_ukuran.items():
        print(f"{k}. {nama} (+Rp {harga:,})")
    pilih_ukuran = input("Pilih (1/2/3): ")
    ukuran_nama, harga_ukuran_pilihan = harga_ukuran.get(pilih_ukuran, ("Sedang", 40000))

    print("\nBerapa tangkai bunga yang diinginkan?")
    try:
        jumlah_tangkai = int(input("(Min 1, Max 50): "))
        if jumlah_tangkai < 1: jumlah_tangkai = 1
        if jumlah_tangkai > 50: jumlah_tangkai = 50
    except:
        jumlah_tangkai = 10

    print("\nApakah ingin menggunakan uang asli di dalam buket?")
    print("1. Ya (+Rp 50,000 biaya jasa)")
    print("2. Tidak")
    pilih_uang = input("Pilih (1/2): ")
    nominal_uang = 0
    if pilih_uang == "1":
        while True:
            try:
                nominal_uang = int(input("Masukkan total uang (100000 - 1000000): "))
                if 100000 <= nominal_uang <= 1000000:
                    break
                else:
                    print("[!] Nominal harus antara 100.000 - 1.000.000")
            except:
                print("[!] Masukkan angka valid")

    bentuk = input("\nMasukkan bentuk atau hiasan buket (maks 20 kata): ")[:100]

    harga_total = harga_dasar + harga_ukuran_pilihan + (jumlah_tangkai * 1000)
    if bunga_asli: harga_total += harga_asli
    if nominal_uang > 0: harga_total += nominal_uang + biaya_uang

    judul = f"Buket {bunga_utama} {warna} {ukuran_nama} ({jumlah_tangkai} tangkai)"
    if bunga_asli: judul += " Asli"
    else: judul += " Palsu"
    if nominal_uang > 0: judul += f" + Uang {nominal_uang:,}"

    harga_final = harga_total
    voucher = False

    if data_pengguna.get('punya_voucher', False):
        konfirmasi_voucher = input(f"\n🎟 Anda punya voucher 50%! Gunakan? (y/n): ").lower()
        if konfirmasi_voucher == "y":
            harga_final = int(harga_total * 0.5)
            voucher = True
            print(f"[🎉] Harga setelah diskon: Rp {harga_final:,}")

    print("\n--- INVOICE ---")
    print(f"Judul Buket : {judul}")
    print(f"Harga Total : Rp {harga_total:,}")
    if voucher:
        print("Diskon      : 50%")
    print(f"Bayar Akhir : Rp {harga_final:,}")
    print(f"Saldo Anda  : Rp {data_pengguna['saldo']:,}")

    if data_pengguna['saldo'] < harga_final:
        print("\n[!] Saldo tidak cukup.")
        time.sleep(2)
        return

    konfirmasi = input("\nPesanan sudah benar? (y/n): ").lower()
    if konfirmasi != "y":
        print("Pesanan dibatalkan.")
        time.sleep(2)
        return

    pesanan_baru = {
        "id": len(muat_pesanan()) + 1,
        "username": data_pengguna['username'],
        "jenis": "kustom",
        "detail": {
            "judul": judul,
            "bunga": bunga_utama,
            "warna": warna,
            "ukuran": ukuran_nama,
            "asli": bunga_asli,
            "tangkai": jumlah_tangkai,
            "bentuk": bentuk,
            "nominal_uang": nominal_uang
        },
        "total_harga": harga_final,
        "status": "pending",
        "voucher_digunakan": voucher
    }

    semua_pesanan = muat_pesanan()
    semua_pesanan.append(pesanan_baru)
    simpan_pesanan(semua_pesanan)

    daftar_pengguna = muat_users()
    for user in daftar_pengguna:
        if user['username'] == data_pengguna['username']:
            user['saldo'] -= harga_final
            if voucher:
                user['punya_voucher'] = False
            break
    simpan_users(daftar_pengguna)

    print("\n[✓] Pesanan berhasil dibuat.")
    
    input("\nTekan Enter untuk kembali...")

'''=================================================================================================================================='''
'''                                                       FUNGSI PESANAN                                                            '''
'''=================================================================================================================================='''

def kelola_pesanan():
  while True:
        bersihkan_layar()
        print("┌──────────────────────────────────┐")
        print("│     🌼 KELOLA STATUS PESANAN 🌼    │")
        print("└──────────────────────────────────┘")

        semua_pesanan = muat_pesanan()
        if not semua_pesanan:
            print("\nBelum ada pesanan.")
            time.sleep(2)
            break 

        tabel = PrettyTable()
        tabel.field_names = ["ID", "Username", "Jenis", "Detail/Item", "Harga", "Status"]
        tabel.align = "l"
        tabel.align["Harga"] = "r"

        for p in semua_pesanan:
            detail = ""
            if p['jenis'] == 'template': 
                detail = p.get('item', {}).get('nama', '')
            elif p['jenis'] == 'kustom':
                if p['detail'].get('tipe') == 'uang': 
                    detail = f"Uang Rp {p['detail'].get('nominal', 0):,}"
                else: 
                    detail = p['detail'].get('pesan', '')
            
            harga_str = f"Rp {p.get('total_harga', 0):,}"
            if p.get('total_harga') is None:
                harga_str = "Belum Ditetapkan"
                
            tabel.add_row([p['id'], p['username'], p['jenis'], detail, harga_str, p['status']])
        
        print(tabel)
        
        print("\nOpsi:")
        print("1. Update Status Pesanan (Otomatis)")
        print("2. Kembali")
        pilihan = input("Pilih Opsi: ")

        if pilihan == '1':
            try:
                idubah = int(input("Masukkan ID Pesanan yang akan diupdate: "))
            except ValueError:
                print("[!] ID harus angka.")
                time.sleep(1)
                continue

            pesanan_target = None
            for p in semua_pesanan:
                if p['id'] == idubah:
                    pesanan_target = p
                    break

            if pesanan_target is None:
                print("[!] ID Pesanan tidak ditemukan.")
                time.sleep(2)
                continue

            print(f"\n--- Mengubah Status Pesanan ID: {idubah} ---")
            print(f"Username: {pesanan_target['username']}")
            print(f"Status Saat Ini: {pesanan_target['status']}")

            status_sekarang = pesanan_target['status']
            jenis_pesanan = pesanan_target['jenis']
            status_baru = status_sekarang 

            if status_sekarang == 'pending':
                status_baru = 'approve'
            
            elif status_sekarang == 'approve':
                if jenis_pesanan == 'kustom':
                    status_baru = 'dirangkai'
                else: 
                    status_baru = 'proses'
            
            elif status_sekarang == 'dirangkai': 
                status_baru = 'proses'
                
            elif status_sekarang == 'proses':
                status_baru = 'selesai'
                
            elif status_sekarang == 'selesai':
                print("[!] Pesanan ini sudah 'selesai'. Tidak bisa diubah lagi.")
                time.sleep(2)
                continue

            pesanan_target['status'] = status_baru
            print(f"[✓] Status berhasil diubah menjadi '{status_baru}'.")

            if status_baru == 'selesai':
                
                stokdikurangi = False
                
                if jenis_pesanan == 'template':
                    daftar_bunga = muat_bunga()
                    item_id_pesanan = pesanan_target.get('item', {}).get('id')
                    
                    if item_id_pesanan is not None:
                        for bunga in daftar_bunga:
                            if bunga['id'] == item_id_pesanan:
                                if bunga['stok'] > 0:
                                    bunga['stok'] = bunga['stok'] - 1
                                    simpan_bunga(daftar_bunga)
                                    print(f"- Stok '{bunga['nama']}' berhasil dikurangi.")
                                    stokdikurangi = True
                                else:
                                    print(f"[!] Stok '{bunga['nama']}' HABIS! Gagal.")
                                    pesanan_target['status'] = 'proses'
                                break
                    else:
                        print("[!] Item bunga tidak ditemukan di data pesanan.")
                
    
                if jenis_pesanan == 'kustom' or stokdikurangi:
                    daftar_pengguna = muat_users()
                    for user in daftar_pengguna:
                        if user['username'] == pesanan_target['username']:
                            user['pembelian_selesai'] = user.get('pembelian_selesai', 0) + 1
                            
                            if user['pembelian_selesai'] % 3 == 0:
                                if user.get('punya_voucher', False) == False:
                                    user['punya_voucher'] = True
                                    print(f"[!] Pengguna mendapatkan voucher!")
                            break
                    simpan_users(daftar_pengguna)
                else:
                    print("[!] Gagal update voucher karena stok template habis.")
            
            simpan_pesanan(semua_pesanan) 
            time.sleep(2)

        elif pilihan == '2':
            break

'''=================================================================================================================================='''
'''                                                       HISTORI                                                         '''
'''=================================================================================================================================='''

def lihat_histori_penjualan():
    bersihkan_layar()
    print("🌷🌼🌷HISTORI PENJUALAN SELESAI🌷🌼🌷")

    pesanan_selesai = sorted(
        [p for p in muat_pesanan() if p.get('status') == 'selesai'],
        key=lambda x: x['id'], reverse=True
    )

    if not pesanan_selesai:
        print("\n>> Belum ada penjualan yang selesai. <<")
    else:
        total_keuntungan = sum(p.get('total_harga', 0) for p in pesanan_selesai)
        print(f"\n>>> TOTAL KEUNTUNGAN: Rp {total_keuntungan:,} <<<")

        tabel = PrettyTable(["ID", "Username", "Jenis", "Detail/Nominal", "Harga Total"])
        tabel.align, tabel.align["Harga Total"] = "l", "r"

        for p in pesanan_selesai:
            if p['jenis'] == 'template':
                detail = p.get('item', {}).get('nama', '')
            elif p['jenis'] == 'kustom':
                d = p.get('detail', {})
                detail = d.get('judul', '')  
            else:
                detail = ""

            tabel.add_row([p['id'], p['username'], p['jenis'], detail, f"Rp {p.get('total_harga', 0):,}"])
        print(tabel)

    input("\nTekan Enter untuk kembali...")

'''=================================================================================================================================='''
'''                                                         MENU ADMIN                                                                '''
'''=================================================================================================================================='''

def menu_admin(mimin):
    while True:
        bersihkan_layar()
        if mimin in ('aya', 'ibrah'):
            print("🌷🌼🌷 KATALOG BUNGA 🌷🌼🌷")
            daftar = muat_bunga()

            if daftar:
                tabel = PrettyTable(["ID", "Nama Buket", "Harga (Rp)", "Stok"])
                tabel.align["Nama Buket"], tabel.align["Harga (Rp)"] = "l", "r"
                for b in daftar:
                    tabel.add_row([b['id'], b['nama'], f"{b['harga']:,}", b['stok']])
                print(tabel)
            else:
                print("\n>> Katalog bunga kosong. <<")

            print("\n┌──────────────────────────────────┐")
            print("│    ⚘ ADMIN PENGELOLA PRODUK ⚘    │")
            print("├──────────────────────────────────┤")
            print("│ 1. Tambah Buket                  │")
            print("│ 2. Update Buket                  │")
            print("│ 3. Hapus Buket                   │")
            print("│ 4. Lihat Histori Penjualan       │") 
            print("│ 5. Logout                        │") 
            print("└──────────────────────────────────┘")

            p = input("Pilih Opsi: ")
            if p == '1': tambah_bunga()
            elif p == '2': ubah_bunga()
            elif p == '3': hapus_bunga()
            elif p == '4': lihat_histori_penjualan()
            elif p == '5': break

        elif mimin == 'carla':
            print("🌷🌼🌷 DAFTAR PESANAN 🌷🌼🌷")
            daftar = muat_pesanan()

            if daftar:
                tabel = PrettyTable(["ID", "User", "Jenis", "Detail", "Harga", "Status"])
                tabel.align, tabel.align["Harga"] = "l", "r"
                for p in daftar:
                    if p['jenis'] == 'template':
                        detail = p.get('item', {}).get('nama', '')
                    elif p['jenis'] == 'kustom':
                        d = p.get('detail', {})
                        detail = d.get('judul', '')  
                    else:
                        detail = ""
                    tabel.add_row([p['id'], p['username'], p['jenis'], detail, f"Rp {p.get('total_harga', 0):,}", p['status']])
                print(tabel)
            else:
                print("\nBelum ada pesanan.")

            print("\n┌──────────────────────────────────┐")
            print("│  ⚘ ADMIN PENGELOLA PESANAN ⚘     │")
            print("├──────────────────────────────────┤")
            print("│ 1. Kelola Status Pesanan         │") 
            print("│ 2. Lihat Histori Penjualan       │") 
            print("│ 3. Logout                        │") 
            print("└──────────────────────────────────┘")

            p = input("Pilih: ")
            if p == '1': kelola_pesanan()
            elif p == '2': lihat_histori_penjualan()
            elif p == '3': break

'''=================================================================================================================================='''
'''                                                         BELANJA PENGGUNA                                                         '''
'''=================================================================================================================================='''

def menu_belanja_pengguna(u):
    while True:
        daftar_pengguna = muat_users()
        
        userbaru = u 
        for user_di_list in daftar_pengguna:
            if user_di_list['username'] == u['username']:
                userbaru = user_di_list 
                break 

        bersihkan_layar()
        print(f"Selamat datang, {userbaru['username']}! Saldo Anda: Rp {userbaru['saldo']:,}")
        
        jml_beli = userbaru.get('pembelian_selesai', 0)
        punya_voucher = userbaru.get('punya_voucher', False) 
        print(f"Anda telah menyelesaikan {jml_beli} pembelian.")
        if punya_voucher:
             print("Selamat! Anda memiliki Voucher Diskon 50% untuk pembelian berikutnya! 🎉")
        elif jml_beli < 3 :
             print(f"Selesaikan {3 - (jml_beli % 3)} pembelian lagi untuk mendapatkan Voucher 50%.")

        print("\n--- KATALOG BUNGA ---")
        daftar_bunga = muat_bunga()
        if not daftar_bunga:
            print(">> Katalog bunga kosong. <<")
        else:
            tabel_bunga = PrettyTable()
            tabel_bunga.field_names = ["ID", "Nama Buket", "Harga (Rp)", "Stok"]
            tabel_bunga.align["Nama Buket"] = "l"
            tabel_bunga.align["Harga (Rp)"] = "r"
            for bunga in daftar_bunga:
                harga_format = f"{bunga['harga']:,}"
                tabel_bunga.add_row([bunga['id'], bunga['nama'], harga_format, bunga['stok']])
            print(tabel_bunga)

        print("\n--- RIWAYAT PEMBELIAN ANDA ---")
        semua_pesanan = muat_pesanan()
        
        history_saya = []
        for p in semua_pesanan:
            if p['username'] == userbaru['username']:
                history_saya.append(p)
        
        history_saya.reverse()
        
        history_tampil = history_saya[:5]

        if not history_tampil:
            print(">> Anda belum pernah melakukan pembelian. <<")
        else:
            tabel_history = PrettyTable()
            tabel_history.field_names = ["ID Pesanan", "Jenis", "Detail/Nominal", "Harga Total", "Status"]
            tabel_history.align = "l"
            tabel_history.align["Harga Total"] = "r"
            
            for p in history_tampil:
                detail = "" 
                if p['jenis'] == 'template': 
                    detail = p.get('item', {}).get('nama', "") 
                elif p['jenis'] == 'kustom':
                    if p.get('detail', {}).get('tipe') == 'uang': 
                        detail = f"Uang Rp {p.get('detail', {}).get('nominal', 0):,}"
                    else: 
                        detail = p.get('detail', {}).get('pesan', p.get('detail', {}).get('judul', '')) 
                
                harga_str = f"Rp {p.get('total_harga', 0):,}"
                if p.get('total_harga') is None:
                     harga_str = "Belum Ditetapkan" 
                    
                tabel_history.add_row([p['id'], p['jenis'], detail, harga_str, p['status']])
            print(tabel_history)

        print("\n┌──────────────────────────────────┐")
        print("│       ⚘ MENU PENGGUNA ⚘          │")
        print("├──────────────────────────────────┤")
        print("│ 1. Beli Bunga                    │")    
        print("│ 2. Top Up Saldo                  │")
        print("│ 3. Logout                        │")
        print("└──────────────────────────────────┘")

        p = input("Pilih: ")
        if p == '1': submenu_beli_bunga(userbaru)
        elif p == '2': topup(userbaru)
        elif p == '3': break

def submenu_beli_bunga(u):
    while True:
        bersihkan_layar()
        print("┌──────────────────────────────────┐")
        print("│         ⚘ BELI BUNGA ⚘           │")
        print("├──────────────────────────────────┤")
        print("│ 1. Pesan Buket Template          │")
        print("│ 2. Pesan Buket Kustom            │")
        print("│ 3. Kembali                       │")
        print("└──────────────────────────────────┘")
        p = input("Pilih opsi: ")
        if p == '1': pesan_buket_template(u)
        elif p == '2': pesan_buket_kustom(u)
        elif p == '3': break
        else:
            print("\n[!] Pilihan tidak valid."); time.sleep(1)

'''=================================================================================================================================='''
'''                                                          MENU LOGIN USER                                                         '''
'''=================================================================================================================================='''

def menu_login_registrasi():
    while True:
        bersihkan_layar()
        print("┌──────────────────────────────────┐")
        print("│         ⚘ MENU LOGIN ⚘           │")
        print("├──────────────────────────────────┤")
        print("│ 1. Login                         │")
        print("│ 2. Registrasi                    │")
        print("│ 3. Kembali ke Menu Utama         │")
        print("└──────────────────────────────────┘")
        p = input("Pilih: ")
        if p == '1':
            if (u := login_user()): menu_belanja_pengguna(u)
        elif p == '2': daftar()
        elif p == '3': break

'''=================================================================================================================================='''
'''                                                             MAIN                                                                  '''
'''=================================================================================================================================='''

def main():
    try:
        while True:
            bersihkan_layar()
            print("┌──────────────────────────────────┐")
            print("│ ⚘ SELAMAT DATANG DI TOKO BUNGA ⚘ │")
            print("├──────────────────────────────────┤")
            print("│ 1. Admin                         │")
            print("│ 2. Pengguna                      │")
            print("│ 3. Keluar                        │")
            print("└──────────────────────────────────┘")
            p = input("Pilih: ")
            if p == '1':
                username = login_admin()
                if username:
                    menu_admin(username)
            elif p == '2': menu_login_registrasi()
            elif p == '3': break 
        
    except KeyboardInterrupt:
        print("\n[!] Program dihentikan oleh pengguna🥀")
         

main()

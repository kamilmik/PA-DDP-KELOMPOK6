# PA-DDP-KELOMPOK6
TEMA : SISTEM MANAJEMEN BOUKET BUNGA 
## KELOMPOK 6 KELAS A
- Kardila Varani Barutu	2509116009
- Rija Aulia Mayatri	2509116011
- Muhammad Ibrahim Kamil	2509116012

## Penjelasan Garis Besar Program: 
Pada program ini, terdapat 2 jenis Akun yaitu Admin dan User,  Admin juga memiliki 2 peran (Peran CRUD dan Peran Mengelola Pesanan)\
Admin CRUD dapat memanipulasi buket (terkhusus buket bunga template) seperti menambahkan, mengedit, dan menghapus. sedangkan\
Admin kelola pesanan memiliki hak untuk mengubah status pesanan (terkhusus buket bunga Kustom). Untuk User, User memiliki\
hak untuk memesan buket - baik itu template maupun kustom - dan juga topup emoney berupa saldo. Terdapat juga sistem login\
Yang dibagi login dan register (untuk pengguna).

## MENU UTAMA :
Pada awal membuka program akan diberi 3 pilihan, 1. Admin, 2. Pengguna, 3.Keluar.\

<img width="363" height="222" alt="image" src="https://github.com/user-attachments/assets/2c322f29-1902-4ca6-98b5-b7a82cec50c1" />\

jika User menginput Ctrl + C maka program akan terhenti dengan output berikut :\
<img width="449" height="274" alt="image" src="https://github.com/user-attachments/assets/eb039a55-46cf-4334-8b31-105adc466d46" />\

Jika User Menginput salah (Selain 1,2 dan 3) maka program akan mengulang kembali meminta User untuk menginput sesuai yang benar.\
Jika User Menginput 1 (Admin) maka program akan dialihkan ke menu login Admin:

## ADMIN :
Terdapat dua Jenis Admin (Aya/Ibrah & Carla) dimana amsing masing memiliki Tugas dan hak masing masing. berikut tampilan Admin saat login berhasil\
<img width="384" height="233" alt="image" src="https://github.com/user-attachments/assets/200d18d0-6df2-420f-830f-3e806b9e7e25" />\

Password Saat login akan di hide menggunakan pwinput. Jika salah menginput Username / Password, maka akan ada tampilan peringatan\
password / username salah, dan diberi kesempatan untuk mengulang sebanyak 3 kali. setelah 3 kali percobaan gagal maka program akan\
mengalihkan kembali ke menu utama setelah 60 detik menunggu (karena hanya testing kami menngunakan 6 detik) : \

<img width="502" height="189" alt="image" src="https://github.com/user-attachments/assets/14e1d300-c2f3-409d-a526-893119b6a6a4" />\

<img width="580" height="263" alt="image" src="https://github.com/user-attachments/assets/0af8fc3a-46cb-4096-b471-3f1f1037c54f" />\

### Admin Aya/Ibrah (CRUD) :
Admin aya & ibrah memiliki hak untuk mengubah, memanipulasi, dan menghapus, serta melihat history penjualan. pada menu utama\
juga menampilkan katalog buket bunga yang dijual. Berikut menu utama Admin CRUD: \
<img width="594" height="470" alt="image" src="https://github.com/user-attachments/assets/59ef79cd-3e66-4822-a9bb-da1c8756baf2" />

- 1. Tambah Buket
     Tambah bunga pada awal, Admin akan menginput Nama buket, harga buket (70.000 - 1.000.000) dan stok (1 - 20) :\
     <img width="584" height="179" alt="image" src="https://github.com/user-attachments/assets/62230624-49cf-41ac-8c4d-e2a5e84d4c99" />\

     dan jika admin salah memasukkan harga dan stok sesuai ketentuan maka program akan memberi peringatan admin salah input.\
     <img width="633" height="275" alt="image" src="https://github.com/user-attachments/assets/ac1cfc4c-a0d6-440f-8c0c-f4f824b9f958" />

     Setelah memasukkan detail bunga selesai, maka program akan menampilkan invoice detail penambahan dan menambahkan data\
     bunga baru ke database bunga.\


     <img width="379" height="257" alt="image" src="https://github.com/user-attachments/assets/713d06f8-17aa-459b-aeae-253e5c20ca7a" />\

- 2. Update Buket
     Setelah admin memilih update buket maka program akan menampilkan list buket yang dijual dan meminta Admin untuk memasukkan id yang\
     ingin diupdate.\
     <img width="517" height="339" alt="image" src="https://github.com/user-attachments/assets/e72cd6e1-b387-4249-9c42-f7b113ee417e" />\

     setelah Admin menginput id buket yang ingin diedit maka program akan memberi input nama, harga, dan stok baru. admin juga bisa\
     skip dengan dikosongkan jika tidak ada yang perlu diupdate.\
     <img width="600" height="444" alt="image" src="https://github.com/user-attachments/assets/3932ea77-a2b0-4f0d-bdd8-ad4ee29f703d" />\

     <img width="311" height="190" alt="image" src="https://github.com/user-attachments/assets/8a54cc96-37df-438c-94ba-e39c5de5678d" />\

     Jika admin salah menginput data(tidak sesuai ketentuan, maka program akan memberi tahu jika Admin salah menginput\
     <img width="674" height="362" alt="image" src="https://github.com/user-attachments/assets/7f5a9a0b-7cbb-45fc-876b-c434b090191c" />


- 3. Hapus Buket
     Setelah admin memilih hapus bunga, maka program akan menampilkan list buket yang dijual dan meminta Admin untuk memasukkan id yang\
     ingin dihapus.\
     <img width="526" height="413" alt="image" src="https://github.com/user-attachments/assets/4ae77bac-f004-4d2a-923e-3fd4629dcd6a" />\

     jika admin salah memasukkan id bunga maka program akan memberi tahu jika admin salah menginput dan meminta untuk input ulang: \
     <img width="528" height="409" alt="image" src="https://github.com/user-attachments/assets/5a04866f-8480-446b-860e-2e26e511121b" />\

- 4. Lihat Histori Penjualan
     Setelah admin memilih hapus bunga, maka program akan menampilkan list Histori penjualan beserta total keuntungan penjualan.\
     <img width="956" height="305" alt="image" src="https://github.com/user-attachments/assets/084806c7-cd67-4117-9b1d-6ca321ebbee8" />\

- 5. Keluar
     Setelah admin memilih Menu keluar maka Admin akan keluar ke menu login admin atau register (log out)

### Admin Carla (kelola Pesanan)
Admin kelola pesanan memiliki hak untuk mengubah status pesanan (terkhusus buket bunga Kustom), juga dapat melihat history penjualan sama seperti\
admin CRUD. berikut Menu admin kelola pesanan setelah login (Carla) :
<img width="995" height="453" alt="image" src="https://github.com/user-attachments/assets/68ee9b02-e916-42d7-9202-0ca1b0408c5b" />


- 1. Kelola Pesanan
     Pada menu ini, admin carla dapat meengelola pesanan dengan memasukkan id, program akan memberi list pesanan dari seluruh status,\
     setelah admin memilih id, program akan mengecek apakah status bisa diubah( pending -> proses -> dirangkai(jika pesanan buket kustom) -> selesai )\
     dan otomatis mengubah jika selain status pesanan selesai. \
     <img width="728" height="400" alt="image" src="https://github.com/user-attachments/assets/9b205a60-2035-4c0e-8957-92fac35ed189" />\
     <img width="444" height="258" alt="image" src="https://github.com/user-attachments/assets/33a37648-0a09-42d1-9a74-c8c862bd2d25" />\
     jika admin salah menginput angka :\
     <img width="418" height="172" alt="image" src="https://github.com/user-attachments/assets/542c60d6-223c-4b00-bb3a-ac869d52c43c" />\

     dan jika admin memilih 2 (kembali) maka admin akan dialihkan ke menu utama kelola pesanan.\
- 2. Lihat Histori Penjualan
     Setelah admin memilih hapus bunga, maka program akan menampilkan list Histori penjualan beserta total keuntungan penjualan.\
     tekan enter untuk kembali ke menu utama admin carla\
     <img width="956" height="305" alt="image" src="https://github.com/user-attachments/assets/084806c7-cd67-4117-9b1d-6ca321ebbee8" />.\















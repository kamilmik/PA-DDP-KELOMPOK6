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

<img width="363" height="222" alt="image" src="https://github.com/user-attachments/assets/2c322f29-1902-4ca6-98b5-b7a82cec50c1" />

jika User menginput Ctrl + C maka program akan terhenti dengan output berikut :\
<img width="449" height="274" alt="image" src="https://github.com/user-attachments/assets/eb039a55-46cf-4334-8b31-105adc466d46" />

Jika User Menginput salah (Selain 1,2 dan 3) maka program akan mengulang kembali meminta User untuk menginput sesuai yang benar.\
Jika User Menginput 1 (Admin) maka program akan dialihkan ke menu login Admin:

## ADMIN :
Terdapat dua Jenis Admin (Aya/Ibrah & Carla) dimana amsing masing memiliki Tugas dan hak masing masing. berikut tampilan Admin saat login berhasil\
<img width="384" height="233" alt="image" src="https://github.com/user-attachments/assets/200d18d0-6df2-420f-830f-3e806b9e7e25" />

Password Saat login akan di hide menggunakan pwinput. Jika salah menginput Username / Password, maka akan ada tampilan peringatan\
password / username salah, dan diberi kesempatan untuk mengulang sebanyak 3 kali. setelah 3 kali percobaan gagal maka program akan\
mengalihkan kembali ke menu utama setelah 60 detik menunggu (karena hanya testing kami menngunakan 6 detik) : \

<img width="502" height="189" alt="image" src="https://github.com/user-attachments/assets/14e1d300-c2f3-409d-a526-893119b6a6a4" />

<img width="580" height="263" alt="image" src="https://github.com/user-attachments/assets/0af8fc3a-46cb-4096-b471-3f1f1037c54f" />

### Admin Aya/Ibrah (CRUD) :
Admin aya & ibrah memiliki hak untuk mengubah, memanipulasi, dan menghapus, serta melihat history penjualan. pada menu utama\
juga menampilkan katalog buket bunga yang dijual. Berikut menu utama Admin CRUD: \
<img width="594" height="470" alt="image" src="https://github.com/user-attachments/assets/59ef79cd-3e66-4822-a9bb-da1c8756baf2" />

- 1. Tambah Buket
     Tambah bunga pada awal, Admin akan menginput Nama buket, harga buket (70.000 - 1.000.000) dan stok (1 - 20) :\
     <img width="584" height="179" alt="image" src="https://github.com/user-attachments/assets/62230624-49cf-41ac-8c4d-e2a5e84d4c99" />

     dan jika admin salah memasukkan harga dan stok sesuai ketentuan maka program akan memberi peringatan admin salah input.\
     <img width="633" height="275" alt="image" src="https://github.com/user-attachments/assets/ac1cfc4c-a0d6-440f-8c0c-f4f824b9f958" />

     Setelah memasukkan detail bunga selesai, maka program akan menampilkan invoice detail penambahan dan menambahkan data\
     bunga baru ke database bunga.\


     <img width="379" height="257" alt="image" src="https://github.com/user-attachments/assets/713d06f8-17aa-459b-aeae-253e5c20ca7a" />

- 2. Update Buket
     Setelah admin memilih update buket maka program akan menampilkan list buket yang dijual dan meminta Admin untuk memasukkan id yang\
     ingin diupdate.\
     <img width="517" height="339" alt="image" src="https://github.com/user-attachments/assets/e72cd6e1-b387-4249-9c42-f7b113ee417e" />

     setelah Admin menginput id buket yang ingin diedit maka program akan memberi input nama, harga, dan stok baru. admin juga bisa\
     skip dengan dikosongkan jika tidak ada yang perlu diupdate.\
     <img width="600" height="444" alt="image" src="https://github.com/user-attachments/assets/3932ea77-a2b0-4f0d-bdd8-ad4ee29f703d" />

     <img width="311" height="190" alt="image" src="https://github.com/user-attachments/assets/8a54cc96-37df-438c-94ba-e39c5de5678d" />

     Jika admin salah menginput data(tidak sesuai ketentuan, maka program akan memberi tahu jika Admin salah menginput\
     <img width="674" height="362" alt="image" src="https://github.com/user-attachments/assets/7f5a9a0b-7cbb-45fc-876b-c434b090191c" />


- 3. Hapus Buket
     Setelah admin memilih hapus bunga, maka program akan menampilkan list buket yang dijual dan meminta Admin untuk memasukkan id yang\
     ingin dihapus.\
     <img width="526" height="413" alt="image" src="https://github.com/user-attachments/assets/4ae77bac-f004-4d2a-923e-3fd4629dcd6a" />

     jika admin salah memasukkan id bunga maka program akan memberi tahu jika admin salah menginput dan meminta untuk input ulang: \
     <img width="528" height="409" alt="image" src="https://github.com/user-attachments/assets/5a04866f-8480-446b-860e-2e26e511121b" />

- 4. Lihat Histori Penjualan
     Setelah admin memilih hapus bunga, maka program akan menampilkan list Histori penjualan beserta total keuntungan penjualan.\
     <img width="956" height="305" alt="image" src="https://github.com/user-attachments/assets/084806c7-cd67-4117-9b1d-6ca321ebbee8" />

- 5. Keluar
     Setelah admin memilih Menu keluar maka Admin akan keluar ke menu login admin atau register (log out)

### Admin Carla (kelola Pesanan)
Admin kelola pesanan memiliki hak untuk mengubah status pesanan (terkhusus buket bunga Kustom), juga dapat melihat history penjualan sama seperti\
admin CRUD. berikut Menu admin kelola pesanan setelah login (Carla) :
<img width="995" height="453" alt="image" src="https://github.com/user-attachments/assets/68ee9b02-e916-42d7-9202-0ca1b0408c5b" />


- 1. Kelola Pesanan
     Pada menu ini, admin carla dapat meengelola pesanan dengan memasukkan id, program akan memberi list pesanan dari seluruh status,
     setelah admin memilih id, program akan mengecek apakah status bisa diubah( pending -> proses -> dirangkai(jika pesanan buket kustom) -> selesai )\
     dan otomatis mengubah jika selain status pesanan selesai. \
     <img width="728" height="400" alt="image" src="https://github.com/user-attachments/assets/9b205a60-2035-4c0e-8957-92fac35ed189" />
     <img width="444" height="258" alt="image" src="https://github.com/user-attachments/assets/33a37648-0a09-42d1-9a74-c8c862bd2d25" />
     jika admin salah menginput angka :\
     <img width="418" height="172" alt="image" src="https://github.com/user-attachments/assets/542c60d6-223c-4b00-bb3a-ac869d52c43c" />

     dan jika admin memilih 2 (kembali) maka admin akan dialihkan ke menu utama kelola pesanan.\
- 2. Lihat Histori Penjualan
     Setelah admin memilih hapus bunga, maka program akan menampilkan list Histori penjualan beserta total keuntungan penjualan.\
     tekan enter untuk kembali ke menu utama admin carla\
     <img width="956" height="305" alt="image" src="https://github.com/user-attachments/assets/084806c7-cd67-4117-9b1d-6ca321ebbee8" />

## USER :
setelah pada menu awal user memilih menu pengguna (2) maka user akan diarahkan untuk memilih opsi 1. login, 2. Register, 3. Kembali.\
<img width="344" height="201" alt="image" src="https://github.com/user-attachments/assets/b0ad26ce-a4e0-4b4e-8546-4d38d8a64034" />

### Login
Setelah User memilih opsi login, program akan memberi input username dan input password pengguna, dan akan mengecek apakah username\
atau password yang diinput ada pada database users, jika iya maka program akan mengalihkan user ke menu user. dan jika tidak sesuai\
maka program akan memberi kesempatan 3 kali percobaan, setelah 3 kali gagal maka program akan memberi waktu tenggat 60 detik \
(6 detik pada program untuk efisiensi percobaan) lalu mengembalikan user ke menu awal, berikut menu login: \
<img width="367" height="235" alt="image" src="https://github.com/user-attachments/assets/e8334630-6b8f-4d3a-8862-6baae8832dbd" />

jika user salah menginput username/ password maka akan memberi peringatan :\
<img width="502" height="162" alt="image" src="https://github.com/user-attachments/assets/e7b07588-c55d-4c13-b136-d646ee00438e" />

Jika sudah 3 kali maka User harus menunggu 60 detik setelah itu lalu di kembalikan ke menu sebelumnya : \
<img width="549" height="251" alt="image" src="https://github.com/user-attachments/assets/aa229298-368c-455d-ab43-46b9d1316962" />

### Register
Setelah User memilih opsi register, program akan memberi input username baru dan input password baru, pertama program akan cek apakah\
apakah username baru ada di database user (jika ada maka program akan menampikan peringatan seperti berikut :)\
<img width="570" height="111" alt="image" src="https://github.com/user-attachments/assets/051a669a-4e76-45e7-8768-39bfdda01767" />

username baru dibatasi 5 - 20 karakter, dan tidak boleh menggunakan angka, berikut jika user salah menginput:\
<img width="860" height="81" alt="image" src="https://github.com/user-attachments/assets/689ea86c-dcb2-4bdc-9a8a-20b2a58f64c4" />

password juga dibatasi 8 - 15 karakter, berikut jika user salah menginput: \
<img width="767" height="212" alt="image" src="https://github.com/user-attachments/assets/1902c737-e051-42b5-b86c-136f749e1f5d" />

### MENU UTAMA
pada menu utama User, program memberi beberapa data, Katalog bunga (Template) yang bisa dibeli, dan data histori transaksi yang\
dilakukan user (yang sedang login), lalu ada menu opsi memilih 1. Beli Bunga, 2. Top Up saldo, 3. Logout. \
<img width="1004" height="649" alt="image" src="https://github.com/user-attachments/assets/be30e1dc-6709-499a-9f13-9f6e60f65164" />

- 1. Beli Bunga
     ketika user memilih opsi beli bunga, maka akan diarahkan lagi pada sub menu dengan 3 opsi.\
     <img width="377" height="207" alt="image" src="https://github.com/user-attachments/assets/a9c2090b-4962-413b-83a0-a3e5a095a37b" />

     - opsi 1. Bunga Template :\
       User akan di beri list katalog bunga untuk memilih id mana yang ingin di beli user, setelah itu program akan cek apakah id\
       yang di input sesuai pada tabel, jika iya maka program akan cek saldo user apakah cukup untuk membeli bunga yang dipilih\
       setiap pembelian yang berhasil user akan dihitung pembelian 1, jika sudah melakukan 3 pembelian maka user mendapatkan\
       voucher sebesar 50 % yang bisa di pakai di pembelian ke 4.\
       <img width="520" height="229" alt="image" src="https://github.com/user-attachments/assets/b7ff0a75-386d-4797-adfe-6fa33ee9336b" />

       jika user salah input id : \
       <img width="487" height="279" alt="image" src="https://github.com/user-attachments/assets/cb244746-1607-4219-ae00-b16e94ee3600" />

       Jika User benar menginput id, maka program akan menanyakan apakah user yakin untuk membeli produk? (y/n) jika user memilih\
       'n' maka program akan mengembalikan user ke menu sebelumnya, dan jika 'y' maka program akan cek apakah saldo user cukup\
       untuk membeli produk, jika ya:\
       <img width="556" height="481" alt="image" src="https://github.com/user-attachments/assets/c6d10dc4-a92b-4265-8024-b84af7fd8333" />

       jika saldo user tidak cukup untuk membeli produk:\
       <img width="610" height="285" alt="image" src="https://github.com/user-attachments/assets/2a0fc32e-6035-40d7-83b1-e96d258f8572" />

       jika user input selain angka : \
       <img width="500" height="287" alt="image" src="https://github.com/user-attachments/assets/4f1a6af2-3d6d-4a4a-b3e6-ecbe190caee9" />

     - opsi 2. Bunga Kustom :\
       pertama user akan ditanya bunga asli atau palsu(jika asli lebih mahal, dan jika palsu murah):\
       <img width="281" height="149" alt="image" src="https://github.com/user-attachments/assets/16a08d5a-efc3-42b0-b0b8-7c04bc324d6c" />

       lalu User akan ditanya jenis bunga nya apa dengan pilihan :\
       <img width="242" height="171" alt="image" src="https://github.com/user-attachments/assets/522093d1-c175-4201-977b-11929069f945" />

       Lalu user akan ditanya warna dominan :\
       <img width="234" height="173" alt="image" src="https://github.com/user-attachments/assets/d8a72f8a-6c4a-4b98-82eb-b051248d4c7d" />

       lalu user akan ditanya ukuran buket, harga tergantung ukuran :\
       <img width="229" height="118" alt="image" src="https://github.com/user-attachments/assets/4a613668-d9cb-4097-b791-d10f2d09a05b" />

       lalu user akan ditanya berapa tangkai yang dipakai dalam buket, satu tangkai memiliki nominal sendiri, maks input tangkai adalah 50:\
       <img width="368" height="63" alt="image" src="https://github.com/user-attachments/assets/9c719aaf-e401-4f2a-b8e4-b8739c3e5316" />

       lalu user akan ditanya apakah buket menggunakan uang asli atau tidak, jika tidak maka program akan melanjutkan pembayaran, jika iya\
       maka user diminta untuk menginput total yang diinginkan (100.000 - 1.000.000) :\
       <img width="483" height="112" alt="image" src="https://github.com/user-attachments/assets/bc42755d-7fea-4bcb-a3e7-1e43c73bb7ba" />

       lalu user akan diminta untuk membeli catatan tambahan dengan memberi maks 20 kata catatan :\
       <img width="783" height="149" alt="image" src="https://github.com/user-attachments/assets/b5356239-b649-4abc-b5fc-77abe351d08f" />

       terakhir user akan diberi program sebuah invoice pembelian, dengan total hitungan yang sudah di kalkulasi, user dapat memilih\
       apakah pesanan sudah tepat atau tidak kembali :\
       <img width="766" height="266" alt="image" src="https://github.com/user-attachments/assets/e1dca023-aa1b-4229-b652-6595a67c2132" />

       maka setelah user mensetujui dan saldo cukup, pesanan akan masuk ke database pesanan, serta dalam status pending dan menunggu\
       diubah oleh admin carla. jika admin carla sudah mengubah status pesanan menjadi selesai, maka user berhasil mendapatkan \
       +1 total pembelian, jika sudah mencapai 3, maka user mendapatkan voucher 50% yang dapat digunakan pada pembelian selanjutnya.
       





 


















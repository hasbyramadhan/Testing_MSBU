# Testing_MSBU


========== MSBU Testing =========
1. Anda dapat langsung menjalankan testing melalui Visual Studio Code (VSCode).
2. Gunakan perintah berikut di terminal VSCode "py MSBU_Testing"


=========== Modul Odoo ===========
1. Salin folder MSBU_Modul_Room_Booking ke direktori Odoo.
2. Buka Odoo dan cari modul Room Booking di bagian aplikasi, kemudian install modul tersebut.
3. Setelah instalasi berhasil, buka modul yang bernama Manajemen Ruangan untuk mulai menggunakan fitur yang tersedia.


==== Testing Running API ====
1. Login untuk Mendapatkan Token
   - Method: POST
   - URL: http://localhost:8069/api/login
   - Headers:
       Content-Type: application/json
   - Body
        {
            "username": "admin",
            "password": "password123"
        }
    - Response:
        {
            "token": "tokengenerated"
        }


2. Mendapatkan Status Booking
   - Method: GET
   - URL: http://localhost:8069/api/booking_status/1
   - Headers:
       Authorization: Bearer <token yg di dapat dari login>
   - Response: Sesuaikan dengan booking ID yang ada.
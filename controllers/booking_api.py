from odoo import http
from odoo.http import request, Response
import json
import logging
import secrets

_logger = logging.getLogger(__name__)

# Deklarasi username dan password statis
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

# Simpan token yang dihasilkan dalam dictionary untuk referensi
valid_tokens = {}

class RoomBookingAPI(http.Controller):

    # Endpoint login untuk mendapatkan token
    @http.route('/api/login', type='json', auth='public', methods=['POST'], csrf=False)
    def login(self):
        try:
            data = json.loads(request.httprequest.data)
            username = data.get('username')
            password = data.get('password')

            _logger.info(f'Meminta login dengan username: {username}')

            if not username or not password:
                return {'error': 'Username dan password harus diisi'}, 400

            if username == VALID_USERNAME and password == VALID_PASSWORD:
                dynamic_token = secrets.token_urlsafe(16)
                valid_tokens[username] = dynamic_token  # Simpan token untuk username
                return {'token': dynamic_token}
            else:
                return {'error': 'Username atau password salah'}, 401

        except json.JSONDecodeError:
            return {'error': 'Invalid JSON data'}, 400

    # Endpoint untuk mendapatkan status booking dengan token validasi
    @http.route('/api/booking_status/<int:booking_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_booking_status(self, booking_id, **kwargs):
        token = request.httprequest.headers.get('Authorization')

        # Validasi token
        if not token or token != f"Bearer {valid_tokens.get(VALID_USERNAME, '')}":
            _logger.error('Token tidak valid atau tidak ada')
            return Response(json.dumps({'error': 'Unauthorized'}), status=401, mimetype='application/json')

        _logger.info(f'Meminta status booking dengan ID: {booking_id}')

        # Mencari booking berdasarkan ID
        booking = request.env['pemesanan.ruangan'].sudo().search([('id', '=', booking_id)], limit=1)
        if not booking:
            _logger.error(f'Booking dengan ID {booking_id} tidak ditemukan')
            return Response(json.dumps({"error": "Booking not found"}), status=404, mimetype='application/json')

        # Mengambil data booking
        try:
            data = {
                "booking_id": booking.id,
                "nomor_pemesanan": booking.nomor_pemesanan or "N/A",
                "ruangan": booking.ruangan_id.nama_ruangan if booking.ruangan_id else "N/A",
                "nama_pemesan": booking.nama_pemesan or "N/A",
                "tanggal_pemesanan": booking.tanggal_pemesanan.isoformat() if booking.tanggal_pemesanan else "N/A",
                "status_pemesanan": booking.status_pemesanan or "N/A",
            }
            _logger.info(f'Data booking: {data}')
        except Exception as e:
            _logger.error(f'Error saat mengakses data booking: {str(e)}')
            return Response(json.dumps({"error": "Internal server error"}), status=500, mimetype='application/json')

        return Response(json.dumps(data), status=200, mimetype='application/json')

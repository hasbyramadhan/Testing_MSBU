{
    'name': 'Manajemen Ruangan',
    'version': '1.0',
    'category': 'Management',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/master_ruangan_views.xml',  # Pastikan file XML view di-include
        'views/pemesanan_ruangan_views.xml',
        'views/room_booking_menu_views.xml',  # Tambahkan jika ada file khusus untuk menu
        'data/sequence_data.xml',  # Tambahkan baris ini
        # 'data/swagger.yaml',
        # 'data/action_cron.xml',

    ],
    'installable': True,
    'application': True,
}

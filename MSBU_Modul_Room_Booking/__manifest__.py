{
    'name': 'Manajemen Ruangan',
    'version': '1.0',
    'category': 'Management',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/master_ruangan_views.xml', 
        'views/pemesanan_ruangan_views.xml',
        'views/room_booking_menu_views.xml',  
        'data/sequence_data.xml', 
        # 'data/action_cron.xml',

    ],
    'installable': True,
    'application': True,
}

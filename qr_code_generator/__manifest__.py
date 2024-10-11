# -*- coding: utf-8 -*-

{
    'name': 'QR Menu',
    'version': '18.0.1.0.0',
    'description': 'To generate QR code',
    'depends': ['base', 'mail', 'web'],
    'data': [
        'views/ir_actions_client.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'qr_code_generator/static/src/xml/qr_image.xml',
            'qr_code_generator/static/src/xml/qr_generator_template.xml',
            'qr_code_generator/static/src/js/qr_code_component.js',
            'qr_code_generator/static/src/xml/qr_code_generator.xml',
            'qr_code_generator/static/src/js/qr_code_generator.js',
        ],
    },
    'installable': True,
}

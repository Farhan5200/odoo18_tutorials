# -*- coding: utf-8 -*-

{
    'name': 'Purchase Order Migration',
    'version': '18.0.1.0.0',
    'summary': 'to migrate purchase order data from odoo17 to odoo18',
    'description': 'to migrate purchase order data from odoo17 to odoo18',
    'depends': ['base', 'purchase', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/odoo_migration_action.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'odoo_migration/static/src/xml/odoo_migration_modal.xml',
            'odoo_migration/static/src/js/odoo_migartion_modal.js',
        ],
    },
    'installable': True,
}

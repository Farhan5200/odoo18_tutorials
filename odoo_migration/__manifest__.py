# -*- coding: utf-8 -*-

{
    'name': 'Purchase Order Migration',
    'version': '18.0.1.0.0',
    'summary': 'to migrate purchase order data from odoo17 to odoo18',
    'description': 'to migrate purchase order data from odoo17 to odoo18',
    'depends': ['base', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/odoo_migration_wizard_views.xml',
    ],
    'installable': True,
}

# -*- coding: utf-8 -*-

{
    'name': 'Multiple Reference Per Product',
    'version': '18.0.1.0.0',
    'summary': 'to add multiple references to a product',
    'description': 'to add multiple references to a product',
    'depends': ['base', 'product', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_product_views.xml',
        'views/multiple_reference_product_views.xml',
    ],
    'installable': True,
}

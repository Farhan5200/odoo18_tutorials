# -*- coding: utf-8 -*-

{
    'name':'Purchase Order Migration',
    'depends':['base','purchase'],
    'data':[
        'security/ir.model.access.csv',
        'wizard/odoo_migration_wizard_views.xml',
    ],
}
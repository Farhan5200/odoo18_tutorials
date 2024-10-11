# -*- coding: utf-8 -*-

{
    'name': 'CRM Dashboard',
    'depends': ['base', 'crm', 'web'],
    'data': [
        'data/client_action.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'crm_dashboard/static/src/js/crm_dashboard.js',
            'crm_dashboard/static/src/xml/crm_dashboard.xml',
        ],
    },

}

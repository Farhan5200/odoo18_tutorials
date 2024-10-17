# -*- coding: utf-8 -*-

{
    'name': 'CRM Dashboard',
    'version': '18.0.1.0.0',
    'summary': 'To create CRM Dashboard',
    'description': 'To create crm darboard containing 5 charts',
    'depends': ['base', 'crm', 'web', 'sale'],
    'data': [
        'data/client_action.xml',
        'views/crm_team_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'crm_dashboard/static/src/js/crm_dashboard.js',
            'crm_dashboard/static/src/xml/crm_dashboard.xml',
            'https://cdn.jsdelivr.net/npm/chart.js',
        ],
    },
    'installable': True,
}

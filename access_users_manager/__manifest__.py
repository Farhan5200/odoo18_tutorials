# -*- coding: utf-8 -*-

{
    'name': 'Access User Access Manager',
    'depends': ['base','web','mail'],
    'data':[
        'security/ir.model.access.csv',
        'views/user_profile_views.xml',
        'views/access_manager_views.xml',
        'views/ir_ui_button_views.xml',
        'data/ir_ui_button_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'access_users_manager/static/src/js/loading_indicator.js',
            'access_users_manager/static/src/js/form_arch_parser.js',
        ],
    },
    'application':True,
}

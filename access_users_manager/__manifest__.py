# -*- coding: utf-8 -*-

{
    'name': 'Access User Access Manager',
    'depends': ['base'],
    'data':[
        'security/ir.model.access.csv',
        'views/user_profile_views.xml',
        'views/access_manager_views.xml',
        'views/ir_ui_button_views.xml',
        'data/ir_ui_button_data.xml',
    ],
    'application':True,
}

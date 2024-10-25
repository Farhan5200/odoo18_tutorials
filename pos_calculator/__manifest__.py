# -*- coding: utf-8 -*-

{
    'name': 'POS Calculator',
    'version': '18.0.1.0.0',
    'summary': 'to add virtual calculator in pos screen',
    'description': 'to add virtual calculator in pos screen',
    'depends': ['base', 'point_of_sale', 'web'],
    'data': [
        'views/calculator_client_action.xml',
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_calculator/static/src/js/pos_calculator_button.js',
            'pos_calculator/static/src/js/pos_calculator_component.js',
            'pos_calculator/static/src/css/pos_calculator.css',
            'pos_calculator/static/src/xml/pos_calculator_button.xml',
            'pos_calculator/static/src/xml/pos_calculator.xml',
        ],
    },
    'installable': True,
}

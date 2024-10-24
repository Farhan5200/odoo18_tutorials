# -*- coding: utf-8 -*-

{
    'name': 'POS Calculator',
    'depends': ['base', 'point_of_sale', 'web'],
    'data':[
      'views/calculator_client_action.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_calculator/static/src/js/pos_calculator_button.js',
            'pos_calculator/static/src/js/pos_calculator_component.js',
            'pos_calculator/static/src/xml/pos_calculator_button.xml',
            'pos_calculator/static/src/xml/pos_calculator.xml',
        ],
    },
}

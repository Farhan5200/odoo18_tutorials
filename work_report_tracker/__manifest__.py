# -*- coding: utf-8 -*-

{
    'name': 'Work Report',
    'version': '18.0.1.0.0',
    'summary': 'To record work report from incomming mail',
    'description': 'To record work report from incomming mail',
    'depends': ['base', 'hr', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/work_report_views.xml',
        'wizard/work_report_pdf_wizard.xml',
        'report/pdf_work_report_templates.xml',
        'report/ir_actions_report.xml',
    ],
    'installable': True,
}

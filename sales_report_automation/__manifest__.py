# -*- coding: utf-8 -*-

{
    'name': 'Sale Report Automation',
    'version': '18.0.1.0.0',
    'summary': 'To send sales report to selected partners automatically',
    'description': 'created a new menu under sales-reporting and send email automatically accourding to the records',
    'depends': ['base', 'sale', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        'data/mail_template.xml',
        'views/sale_report_automation_views.xml',
        'data/cron_data.xml',
        'report/sale_pdf_report_template.xml',
        'report/ir_actions_report.xml',
    ],
    'installable': True,
}

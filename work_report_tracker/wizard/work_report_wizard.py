# -*- coding: utf-8 -*-

from odoo import fields,models

class WorkReportWizard(models.TransientModel):
    _name = 'work.report.wizard'

    employee_ids = fields.Many2many('hr.employee', string='Employees')
    period = fields.Selection([
        ('today','Today'),
        ('this_month','This Month'),
        ('this_year', 'This Year')
    ], string='Period')


    def action_print_pdf_work_report(self):
        """function to print pdf report"""
        data = {
            'selected_employees' : self.employee_ids.ids,
            'selected_period': self.period
        }
        return self.env.ref('work_report_tracker.action_work_report_pdf').report_action(None, data=data)

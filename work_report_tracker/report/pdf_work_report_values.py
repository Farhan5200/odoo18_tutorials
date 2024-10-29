# -*- coding: utf-8 -*-


from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools import date_utils


class SalePDFReportValues(models.AbstractModel):
    """to pass datas to the report"""
    _name = "report.work_report_tracker.pdf_work_report_templates"
    _description = "Pdf Work Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        """to pass datas to pdf report"""
        employees = self.env['hr.employee'].browse(data['selected_employees'])
        period = data['selected_period']
        today = fields.Date.today()
        from_date = today
        to_date = today

        query = """select distinct employee_id from work_report"""
        self.env.cr.execute(query)
        result = self.env.cr.dictfetchall()
        all_report_emp_id = [i['employee_id'] for i in result]


        if period == 'this_month':
            from_date = date_utils.start_of(today, "month")
            to_date = date_utils.end_of(today, "month")

        if period == 'this_year':
            from_date = date_utils.start_of(today, "year")
            to_date = date_utils.end_of(today, "year")

        if period:
            reports = self.env['work.report'].search([('create_date', '>=', from_date), ('create_date', '<=', to_date)])
            result = reports.read()
            all_report_emp_id = [i['employee_id'][0] for i in result if i['employee_id'][0]]
            all_report_emp_id = list(set(all_report_emp_id))
        else:
            reports = self.env['work.report'].search([])

        all_work_emp = self.env['hr.employee'].browse(all_report_emp_id)
        if reports:
            return {
                'selected_employee':employees,
                'reports':reports,
                'all_report_emp_id':all_report_emp_id,
                'all_work_emp':all_work_emp,
                'period':period,
                'from_date':from_date,
                'to_date':to_date,
            }
        else:
            raise UserError('No records found....!')

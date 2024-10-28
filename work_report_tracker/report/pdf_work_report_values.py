# -*- coding: utf-8 -*-


from odoo import api, fields, models
from odoo.tools import date_utils


class SalePDFReportValues(models.AbstractModel):
    _name = "report.work_report_tracker.pdf_work_report_templates"
    _description = "Pdf Work Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        """to pass datas to pdf report"""
        test='hi'
        print(test,'test')

        return {
            'test':test,
        }

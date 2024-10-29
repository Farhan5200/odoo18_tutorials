# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from odoo import api, fields, models


class WorkReport(models.Model):
    """to record work report from incomming mail"""
    _name = 'work.report'
    _description = 'Work Report'
    _inherit = 'mail.thread'

    name = fields.Char(required=True)
    employee_id = fields.Many2one('hr.employee', string="Employee")
    report = fields.Html()

    @api.model
    def message_new(self, msg_dict, custom_values=None):
        """to insert values from mail to appropriate fields"""
        employee = self.env['res.partner'].browse(msg_dict.get('author_id', False)).employee_ids.id
        defaults = {
            'name': msg_dict.get('subject'),
            'report': msg_dict.get('body'),
            'employee_id': employee,
        }
        return super().message_new(msg_dict, custom_values=defaults)

# -*- coding: utf-8 -*-

import base64
from odoo import _, api, fields, models
from odoo.tools import date_utils


class SaleReportAutomation(models.Model):
    _name = "sale.report.automation"
    _description = "Sale Report Automation"

    name = fields.Char("Sequence no", required=True, default=lambda self: _('New'), copy=False, readonly=True,
                       tracking=True)
    company_id = fields.Many2one("res.company", string="School", tracking=True,
                                 default=lambda self: self.env.company)
    report_type = fields.Selection([
        ('monthly', 'Monthly'),
        ('weekly', 'Weekly'),
    ], string="Report type", default="monthly", required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('running', 'Running'),
        ('cancelled', 'Cancelled')
    ], default="draft")

    from_date = fields.Date(string="From")
    to_date = fields.Date(string="To")
    sales_team_id = fields.Many2one('crm.team', string="Sales Team")
    partner_ids = fields.Many2many('res.partner', string="Customer")

    def action_send_sales_report(self):
        """this function will be triggered by the scheduled action function this function will send mail to each partner
        with attachment of their weekly or monthly sales pdf report"""
        users_obj = self.env['res.users']
        manager_mail = ''
        for user in users_obj.search([]):
            if user.has_group("sales_team.group_sale_manager"):
                manager_mail += f'{user.partner_id.email} '
        if self.state == 'running':
            for rec in self.partner_ids:
                select_partner = []
                select_partner.append(rec.id)
                data = {
                    'selected_interval': self.report_type,
                    'selected_from_date': self.from_date,
                    'selected_to_date': self.to_date,
                    'selected_sales_team': self.sales_team_id.id,
                    'selected_partner': select_partner,
                }
                start_date = self.from_date
                end_date = self.to_date
                today_date = fields.Date.today()
                this_month_start = date_utils.start_of(today_date, "month")
                this_month_end = date_utils.end_of(today_date, "month")
                this_week_start = date_utils.start_of(today_date, "week")
                this_week_end = date_utils.end_of(today_date, "week")
                if self.report_type == 'monthly':
                    """send email for monthly report"""
                    if (start_date <= today_date) and (end_date >= today_date):
                        if today_date == this_month_end:
                            sale_report = self.env.ref('sales_report_automation.action_report_sale_pdf')
                            data_record = base64.b64encode(
                                self.env['ir.actions.report'].sudo()._render_qweb_pdf(sale_report, [self.id],
                                                                                      data=data)[0])
                            ir_values = {
                                'name': f'Sale report of {rec.name} from {this_month_start} to {this_month_end}',
                                'type': 'binary',
                                'datas': data_record,
                                'store_fname': data_record,
                                'mimetype': 'application/pdf',
                                'res_model': 'sale.report.automation',
                            }
                            sale_report_attachment_id = self.env['ir.attachment'].sudo().create(ir_values)
                            if sale_report_attachment_id:
                                email_template = self.env.ref(
                                    'sales_report_automation.sale_report_mail_template')
                                if rec.email:
                                    email = rec.email
                                else:
                                    email = 'admin@example.com'
                                if email_template and email:
                                    email_values = {
                                        'email_to': email,
                                        'email_cc': manager_mail,
                                        'scheduled_date': False,
                                        'recipient_ids': [],
                                        'partner_ids': [],
                                        'auto_delete': True,
                                    }
                                    email_template.attachment_ids = [fields.Command.link(sale_report_attachment_id.id)]
                                    email_template.with_context(context={'partner_name': rec.name,
                                                                         'report_type': 'Monthly',
                                                                         'from_date': this_month_start,
                                                                         'to_date': this_month_end,
                                                                         }).send_mail(
                                        self.id, email_values=email_values, force_send=True)
                                    email_template.attachment_ids = [fields.Command.clear()]
                else:
                    """send mail for weekly report"""
                    if (start_date <= today_date) and (end_date >= today_date):
                        if today_date == this_week_end:
                            sale_report = self.env.ref('sales_report_automation.action_report_sale_pdf')
                            data_record = base64.b64encode(
                                self.env['ir.actions.report'].sudo()._render_qweb_pdf(sale_report, [self.id],
                                                                                      data=data)[0])
                            ir_values = {
                                'name': f'Sale report of {rec.name} from {this_week_start} to {this_week_end}',
                                'type': 'binary',
                                'datas': data_record,
                                'store_fname': data_record,
                                'mimetype': 'application/pdf',
                                'res_model': 'sale.report.automation',
                            }
                            sale_report_attachment_id = self.env['ir.attachment'].sudo().create(ir_values)
                            if sale_report_attachment_id:
                                email_template = self.env.ref(
                                    'sales_report_automation.sale_report_mail_template')
                                if rec.email:
                                    email = rec.email
                                else:
                                    email = 'admin@example.com'
                                if email_template and email:
                                    email_values = {
                                        'email_to': email,
                                        'email_cc': manager_mail,
                                        'scheduled_date': False,
                                        'recipient_ids': [],
                                        'partner_ids': [],
                                        'auto_delete': True,
                                    }
                                    email_template.attachment_ids = [fields.Command.link(sale_report_attachment_id.id)]
                                    email_template.with_context(context={'partner_name': rec.name,
                                                                         'report_type': 'Weekly',
                                                                         'from_date': this_week_start,
                                                                         'to_date': this_week_end,
                                                                         }).send_mail(
                                        self.id, email_values=email_values, force_send=True)
                                    email_template.attachment_ids = [fields.Command.clear()]

    def scheduled_action_send_mail(self):
        """function triggered by scheduled action"""
        events = self.search([])
        for rec in events:
            rec.action_send_sales_report()

    def action_print_sale_pdf_report(self):
        """function to print pdf report"""
        data = {
            'selected_interval': self.report_type,
            'selected_from_date': self.from_date,
            'selected_to_date': self.to_date,
            'selected_sales_team': self.sales_team_id.id,
            'selected_partner': self.partner_ids.ids,
        }

        return self.env.ref('sales_report_automation.action_report_sale_pdf').report_action(None, data=data)

    @api.model_create_multi
    def create(self, vals_list):
        """ Create a sequence """
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = (self.env['ir.sequence'].
                                next_by_code('sale.report.automation'))
        return super().create(vals_list)

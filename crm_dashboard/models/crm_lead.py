# -*- coding: utf-8 -*-

from odoo import api, models

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def get_tiles_data(self):
        company_id = self.env.company
        user_id = self.env.user.id
        revenue = 0
        leads = self.search([('company_id', '=', company_id.id),
                             ('user_id', '=', self.env.user.id)])
        my_leads = leads.filtered(lambda r: r.type == 'lead')
        my_opportunity = leads.filtered(lambda r: r.type == 'opportunity')
        my_lost = self.search([('company_id', '=', company_id.id),
                             ('user_id', '=', self.env.user.id),('active', '=', False)])
        for rec in my_leads:
            print(rec.medium_id.color)
        won = 0
        for records in my_opportunity:
            if records.order_ids:
                won += 1
                for rec in records.order_ids:
                    if rec.invoice_ids:
                        revenue += sum(rec.invoice_ids.mapped('amount_total'))
        win_ratio = f'{won}/{len(my_lost)}'
        currency = company_id.currency_id.symbol
        expected_revenue = sum(my_opportunity.mapped('expected_revenue'))
        return {
            'total_leads': len(my_leads),
            'total_opportunity': len(my_opportunity),
            'expected_revenue': expected_revenue,
            'currency': currency,
            'revenue': revenue,
            'user_id':user_id,
            'company_id':company_id.id,
            'win_ratio':win_ratio,
        }

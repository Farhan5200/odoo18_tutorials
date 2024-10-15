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
        self.doughnut_chart_values()
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

    @api.model
    def doughnut_chart_values(self):
        leads = self.search([('company_id', '=', self.env.company.id),
                             ('user_id', '=', self.env.user.id), ('type', '=', 'lead')])
        medium_labels = []
        for rec in leads:
            if rec.medium_id.name not in medium_labels:
                medium_labels.append(rec.medium_id.name)

        medium_count = []
        for i in range(0,len(medium_labels)):
            medium_count.append(0)
            for rec in leads:
                if medium_labels[i] == rec.medium_id.name:
                    medium_count[i] += 1

        return{
            'medium_labels':medium_labels,
            'medium_count':medium_count,
        }

    @api.model
    def pie_chart_values(self):
        leads = self.search([('company_id', '=', self.env.company.id),
                             ('user_id', '=', self.env.user.id)])
        label_activity_type = []
        label_activity_type_count = []
        for rec in leads:
            for records in rec.activity_ids:
                if records.activity_type_id.name not in label_activity_type:
                    label_activity_type.append(records.activity_type_id.name)
                    label_activity_type_count.append(0)

        for rec in leads:
            for records in rec.activity_ids:
                for i in range(0,len(label_activity_type)):
                    if label_activity_type[i] == records.activity_type_id.name:
                        label_activity_type_count[i] += 1

        return{
            'label_activity_type':label_activity_type,
            'label_activity_type_count':label_activity_type_count,
        }

    @api.model
    def doughnut_chart_values_campaign(self):
        leads = self.search([('company_id', '=', self.env.company.id),
                             ('user_id', '=', self.env.user.id), ('type', '=', 'lead')])
        campaign_labels = []
        for rec in leads:
            if rec.campaign_id.name not in campaign_labels:
                campaign_labels.append(rec.campaign_id.name)

        campaign_count = []
        for i in range(0, len(campaign_labels)):
            campaign_count.append(0)
            for rec in leads:
                if campaign_labels[i] == rec.campaign_id.name:
                    campaign_count[i] += 1

        return{
            'campaign_labels':campaign_labels,
            'campaign_count':campaign_count,
        }

    @api.model
    def bar_chart_values(self):
        lost = self.search([('company_id', '=', self.env.company.id),
                             ('user_id', '=', self.env.user.id), ('active', '=', False)])
        lost_leads = lost.filtered(lambda r: r.type == 'lead')
        lost_oppertunity = lost.filtered(lambda r: r.type == 'opportunity')
        lost_count = []
        lost_count.append(len(lost_leads))
        lost_count.append(len(lost_oppertunity))
        return{
          'lost_count':lost_count,
        }

# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.tools import date_utils
from dateutil.relativedelta import relativedelta
import calendar
import datetime


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def calculate_quater(self):
        """to claculate which quater is today"""
        today_date = fields.Date.today()
        first_quater_from = date_utils.start_of(today_date, "year")
        second_quater_from = first_quater_from + relativedelta(months=+ 3)
        third_quater_from = second_quater_from + relativedelta(months=+ 3)
        forth_quater_from = third_quater_from + relativedelta(months=+ 3)
        forth_quater_end = date_utils.end_of(today_date, "year")
        if today_date >= first_quater_from and today_date < second_quater_from:
            return first_quater_from
        elif today_date >= second_quater_from and today_date < third_quater_from:
            return second_quater_from
        elif today_date >= third_quater_from and today_date < forth_quater_from:
            return third_quater_from
        elif today_date >= forth_quater_from and today_date <= forth_quater_end:
            return forth_quater_from

    def calculate_from_and_to_date(self, selected_period):
        """to calculate dates"""
        today_date = fields.Date.today()
        if selected_period == 'this_year':
            from_date = date_utils.start_of(today_date, "year")
            to_date = date_utils.end_of(today_date, "year")
        elif selected_period == 'this_month':
            from_date = date_utils.start_of(today_date, "month")
            to_date = date_utils.end_of(today_date, "month")
        elif selected_period == 'this_week':
            from_date = date_utils.start_of(today_date, "week")
            to_date = date_utils.end_of(today_date, "week")
        return from_date,to_date


    @api.model
    def get_tiles_data(self, selected_period, isManager):
        """to pass tiles data"""
        today_date = fields.Date.today()
        company_id = self.env.company
        user_id = self.env.user.id
        revenue = 0
        leads = self.search([('company_id', '=', company_id.id)])
        my_lost = self.search([('company_id', '=', company_id.id), ('active', '=', False)])
        if isManager:
            if selected_period == 'this_year':
                from_date = date_utils.start_of(today_date, "year")
                to_date = date_utils.end_of(today_date, "year")
                leads = self.search([('company_id', '=', company_id.id), ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date)])
                my_lost = self.search([('company_id', '=', company_id.id),
                                       ('active', '=', False), ('create_date', '>=', from_date),
                                       ('create_date', '<=', to_date)])
            elif selected_period == 'this_quater':
                this_quater_start = self.calculate_quater()
                this_quater_end = this_quater_start + relativedelta(months=+ 3)
                leads = self.search([('company_id', '=', company_id.id),
                                     ('create_date', '>=', this_quater_start),
                                     ('create_date', '<', this_quater_end)])
                my_lost = self.search([('company_id', '=', company_id.id),
                                       ('active', '=', False), ('create_date', '>=', this_quater_start),
                                       ('create_date', '<', this_quater_end)])
            elif selected_period == 'this_month':
                from_date = date_utils.start_of(today_date, "month")
                to_date = date_utils.end_of(today_date, "month")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date)])
                my_lost = self.search([('company_id', '=', company_id.id),
                                       ('active', '=', False), ('create_date', '>=', from_date),
                                       ('create_date', '<=', to_date)])
            elif selected_period == 'this_week':
                from_date = date_utils.start_of(today_date, "week")
                to_date = date_utils.end_of(today_date, "week")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date)])
                my_lost = self.search([('company_id', '=', company_id.id),
                                       ('active', '=', False), ('create_date', '>=', from_date),
                                       ('create_date', '<=', to_date)])
        else:
            if selected_period == 'this_year':
                from_date = date_utils.start_of(today_date, "year")
                to_date = date_utils.end_of(today_date, "year")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('create_date', '>=', from_date),
                                     ('user_id', '=', self.env.user.id),
                                     ('create_date', '<=', to_date)])
                my_lost = self.search([('company_id', '=', company_id.id),
                                       ('user_id', '=', self.env.user.id), ('active', '=', False),
                                       ('create_date', '>=', from_date),
                                       ('create_date', '<=', to_date)])
            elif selected_period == 'this_quater':
                this_quater_start = self.calculate_quater()
                this_quater_end = this_quater_start + relativedelta(months=+ 3)
                leads = self.search([('company_id', '=', company_id.id),
                                     ('user_id', '=', self.env.user.id), ('create_date', '>=', this_quater_start),
                                     ('create_date', '<', this_quater_end)])
                my_lost = self.search([('company_id', '=', company_id.id),
                                       ('user_id', '=', self.env.user.id), ('active', '=', False),
                                       ('create_date', '>=', this_quater_start),
                                       ('create_date', '<', this_quater_end)])
            elif selected_period == 'this_month':
                from_date = date_utils.start_of(today_date, "month")
                to_date = date_utils.end_of(today_date, "month")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('user_id', '=', self.env.user.id), ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date)])
                my_lost = self.search([('company_id', '=', company_id.id),
                                       ('user_id', '=', self.env.user.id), ('active', '=', False),
                                       ('create_date', '>=', from_date),
                                       ('create_date', '<=', to_date)])
            elif selected_period == 'this_week':
                from_date = date_utils.start_of(today_date, "week")
                to_date = date_utils.end_of(today_date, "week")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('user_id', '=', self.env.user.id), ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date)])
                my_lost = self.search([('company_id', '=', company_id.id),
                                       ('user_id', '=', self.env.user.id), ('active', '=', False),
                                       ('create_date', '>=', from_date),
                                       ('create_date', '<=', to_date)])
        my_leads = leads.filtered(lambda r: r.type == 'lead')
        my_opportunity = leads.filtered(lambda r: r.type == 'opportunity')
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
            'user_id': user_id,
            'company_id': company_id.id,
            'win_ratio': win_ratio,
        }

    @api.model
    def doughnut_chart_values(self, selected_period='all', isManager=False):
        """to pass doughnet chart leads by medium values"""
        today_date = fields.Date.today()
        company_id = self.env.company
        leads = self.search([('company_id', '=', self.env.company.id), ('type', '=', 'lead')])
        if isManager:
            if selected_period == 'this_year':
                from_date = date_utils.start_of(today_date, "year")
                to_date = date_utils.end_of(today_date, "year")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date), ('type', '=', 'lead')])
            elif selected_period == 'this_quater':
                this_quater_start = self.calculate_quater()
                this_quater_end = this_quater_start + relativedelta(months=+ 3)
                leads = self.search([('company_id', '=', company_id.id),
                                     ('create_date', '>=', this_quater_start),
                                     ('create_date', '<', this_quater_end), ('type', '=', 'lead')])
            elif selected_period == 'this_month':
                from_date = date_utils.start_of(today_date, "month")
                to_date = date_utils.end_of(today_date, "month")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date), ('type', '=', 'lead')])
            elif selected_period == 'this_week':
                from_date = date_utils.start_of(today_date, "week")
                to_date = date_utils.end_of(today_date, "week")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date), ('type', '=', 'lead')])
        else:
            if selected_period == 'this_year':
                from_date = date_utils.start_of(today_date, "year")
                to_date = date_utils.end_of(today_date, "year")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('user_id', '=', self.env.user.id), ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date), ('type', '=', 'lead')])
            elif selected_period == 'this_quater':
                this_quater_start = self.calculate_quater()
                this_quater_end = this_quater_start + relativedelta(months=+ 3)
                leads = self.search([('company_id', '=', company_id.id),
                                     ('user_id', '=', self.env.user.id), ('create_date', '>=', this_quater_start),
                                     ('create_date', '<', this_quater_end), ('type', '=', 'lead')])
            elif selected_period == 'this_month':
                from_date = date_utils.start_of(today_date, "month")
                to_date = date_utils.end_of(today_date, "month")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('user_id', '=', self.env.user.id), ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date), ('type', '=', 'lead')])
            elif selected_period == 'this_week':
                from_date = date_utils.start_of(today_date, "week")
                to_date = date_utils.end_of(today_date, "week")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('user_id', '=', self.env.user.id), ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date), ('type', '=', 'lead')])

        medium_labels = []
        for rec in leads:
            if rec.medium_id.name not in medium_labels:
                medium_labels.append(rec.medium_id.name)

        medium_count = []
        for i in range(0, len(medium_labels)):
            medium_count.append(0)
            for rec in leads:
                if medium_labels[i] == rec.medium_id.name:
                    medium_count[i] += 1

        return {
            'medium_labels': medium_labels,
            'medium_count': medium_count,
        }

    @api.model
    def pie_chart_values(self, selected_period='all', isManager=False):
        """to pass pie chart activities values"""
        today_date = fields.Date.today()
        company_id = self.env.company
        leads = self.search([('company_id', '=', self.env.company.id)])
        if isManager:
            if selected_period == 'this_year':
                from_date = date_utils.start_of(today_date, "year")
                to_date = date_utils.end_of(today_date, "year")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date)])
            elif selected_period == 'this_quater':
                this_quater_start = self.calculate_quater()
                this_quater_end = this_quater_start + relativedelta(months=+ 3)
                leads = self.search([('company_id', '=', company_id.id),
                                     ('create_date', '>=', this_quater_start),
                                     ('create_date', '<', this_quater_end)])
            elif selected_period == 'this_month':
                from_date = date_utils.start_of(today_date, "month")
                to_date = date_utils.end_of(today_date, "month")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date)])
            elif selected_period == 'this_week':
                from_date = date_utils.start_of(today_date, "week")
                to_date = date_utils.end_of(today_date, "week")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date)])
        else:
            if selected_period == 'this_year':
                from_date = date_utils.start_of(today_date, "year")
                to_date = date_utils.end_of(today_date, "year")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('user_id', '=', self.env.user.id), ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date)])
            elif selected_period == 'this_quater':
                this_quater_start = self.calculate_quater()
                this_quater_end = this_quater_start + relativedelta(months=+ 3)
                leads = self.search([('company_id', '=', company_id.id),
                                     ('user_id', '=', self.env.user.id), ('create_date', '>=', this_quater_start),
                                     ('create_date', '<', this_quater_end)])
            elif selected_period == 'this_month':
                from_date = date_utils.start_of(today_date, "month")
                to_date = date_utils.end_of(today_date, "month")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('user_id', '=', self.env.user.id), ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date)])
            elif selected_period == 'this_week':
                from_date = date_utils.start_of(today_date, "week")
                to_date = date_utils.end_of(today_date, "week")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('user_id', '=', self.env.user.id), ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date)])

        label_activity_type = []
        label_activity_type_count = []
        for rec in leads:
            for records in rec.activity_ids:
                if records.activity_type_id.name not in label_activity_type:
                    label_activity_type.append(records.activity_type_id.name)
                    label_activity_type_count.append(0)

        for rec in leads:
            for records in rec.activity_ids:
                for i in range(0, len(label_activity_type)):
                    if label_activity_type[i] == records.activity_type_id.name:
                        label_activity_type_count[i] += 1

        return {
            'label_activity_type': label_activity_type,
            'label_activity_type_count': label_activity_type_count,
        }

    @api.model
    def doughnut_chart_values_campaign(self, selected_period='all', isManager=False):
        """to pass doughnet chart leads by campaign values"""
        today_date = fields.Date.today()
        company_id = self.env.company
        leads = self.search([('company_id', '=', self.env.company.id),
                             ('type', '=', 'lead')])
        if isManager:
            if selected_period == 'this_year':
                from_date = date_utils.start_of(today_date, "year")
                to_date = date_utils.end_of(today_date, "year")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date), ('type', '=', 'lead')])
            elif selected_period == 'this_quater':
                this_quater_start = self.calculate_quater()
                this_quater_end = this_quater_start + relativedelta(months=+ 3)
                leads = self.search([('company_id', '=', company_id.id),
                                     ('create_date', '>=', this_quater_start),
                                     ('create_date', '<', this_quater_end), ('type', '=', 'lead')])
            elif selected_period == 'this_month':
                from_date = date_utils.start_of(today_date, "month")
                to_date = date_utils.end_of(today_date, "month")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date), ('type', '=', 'lead')])
            elif selected_period == 'this_week':
                from_date = date_utils.start_of(today_date, "week")
                to_date = date_utils.end_of(today_date, "week")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date), ('type', '=', 'lead')])
        else:
            if selected_period == 'this_year':
                from_date = date_utils.start_of(today_date, "year")
                to_date = date_utils.end_of(today_date, "year")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('user_id', '=', self.env.user.id), ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date), ('type', '=', 'lead')])
            elif selected_period == 'this_quater':
                this_quater_start = self.calculate_quater()
                this_quater_end = this_quater_start + relativedelta(months=+ 3)
                leads = self.search([('company_id', '=', company_id.id),
                                     ('user_id', '=', self.env.user.id), ('create_date', '>=', this_quater_start),
                                     ('create_date', '<', this_quater_end), ('type', '=', 'lead')])
            elif selected_period == 'this_month':
                from_date = date_utils.start_of(today_date, "month")
                to_date = date_utils.end_of(today_date, "month")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('user_id', '=', self.env.user.id), ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date), ('type', '=', 'lead')])
            elif selected_period == 'this_week':
                from_date = date_utils.start_of(today_date, "week")
                to_date = date_utils.end_of(today_date, "week")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('user_id', '=', self.env.user.id), ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date), ('type', '=', 'lead')])

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

        return {
            'campaign_labels': campaign_labels,
            'campaign_count': campaign_count,
        }

    @api.model
    def bar_chart_values(self, selected_period='all', isManager=False):
        """to pass bar chart lost opportunity/lead values"""
        today_date = fields.Date.today()
        company_id = self.env.company
        leads = self.search([('company_id', '=', self.env.company.id),
                             ('active', '=', False)])
        if isManager:
            if selected_period == 'this_year':
                from_date = date_utils.start_of(today_date, "year")
                to_date = date_utils.end_of(today_date, "year")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date), ('active', '=', False)])
            elif selected_period == 'this_quater':
                this_quater_start = self.calculate_quater()
                this_quater_end = this_quater_start + relativedelta(months=+ 3)
                leads = self.search([('company_id', '=', company_id.id),
                                     ('create_date', '>=', this_quater_start),
                                     ('create_date', '<', this_quater_end), ('active', '=', False)])
            elif selected_period == 'this_month':
                from_date = date_utils.start_of(today_date, "month")
                to_date = date_utils.end_of(today_date, "month")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date), ('active', '=', False)])
            elif selected_period == 'this_week':
                from_date = date_utils.start_of(today_date, "week")
                to_date = date_utils.end_of(today_date, "week")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date), ('active', '=', False)])
        else:
            if selected_period == 'this_year':
                from_date = date_utils.start_of(today_date, "year")
                to_date = date_utils.end_of(today_date, "year")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('user_id', '=', self.env.user.id), ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date), ('active', '=', False)])
            elif selected_period == 'this_quater':
                this_quater_start = self.calculate_quater()
                this_quater_end = this_quater_start + relativedelta(months=+ 3)
                leads = self.search([('company_id', '=', company_id.id),
                                     ('user_id', '=', self.env.user.id), ('create_date', '>=', this_quater_start),
                                     ('create_date', '<', this_quater_end), ('active', '=', False)])
            elif selected_period == 'this_month':
                from_date = date_utils.start_of(today_date, "month")
                to_date = date_utils.end_of(today_date, "month")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('user_id', '=', self.env.user.id), ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date), ('active', '=', False)])
            elif selected_period == 'this_week':
                from_date = date_utils.start_of(today_date, "week")
                to_date = date_utils.end_of(today_date, "week")
                leads = self.search([('company_id', '=', company_id.id),
                                     ('user_id', '=', self.env.user.id), ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date), ('active', '=', False)])
        lost_leads = leads.filtered(lambda r: r.type == 'lead')
        lost_oppertunity = leads.filtered(lambda r: r.type == 'opportunity')
        lost_count = []
        lost_count.append(len(lost_leads))
        lost_count.append(len(lost_oppertunity))
        return {
            'lost_count': lost_count,
        }

    @api.model
    def table_values(self, isManager, selected_option):
        """to pass table leads by month values"""
        print(isManager,'kkll')
        today_date = fields.Date.today()
        if isManager:
            if selected_option == 'all':
                leads = self.search([('company_id', '=', self.env.company.id),
                                     ('type', '=', 'lead')], order='create_date')
            elif selected_option == 'this_month':
                from_date = date_utils.start_of(today_date, "month")
                to_date = date_utils.end_of(today_date, "month")
                leads = self.search([('company_id', '=', self.env.company.id),
                                     ('type', '=', 'lead'), ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date)], order='create_date')
            elif selected_option == 'previous_month':
                from_date = date_utils.start_of(today_date, "month") + relativedelta(months=- 1)
                to_date = date_utils.end_of(today_date, "month") + relativedelta(months=- 1)
                leads = self.search([('company_id', '=', self.env.company.id),
                                     ('type', '=', 'lead'), ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date)], order='create_date')
        else:
            if selected_option == 'all':
                leads = self.search([('company_id', '=', self.env.company.id),
                                     ('user_id', '=', self.env.user.id), ('type', '=', 'lead')], order='create_date')
            elif selected_option == 'this_month':
                from_date = date_utils.start_of(today_date, "month")
                to_date = date_utils.end_of(today_date, "month")
                leads = self.search([('company_id', '=', self.env.company.id), ('user_id', '=', self.env.user.id),
                                     ('type', '=', 'lead'), ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date)], order='create_date')
            elif selected_option == 'previous_month':
                from_date = date_utils.start_of(today_date, "month") + relativedelta(months=- 1)
                to_date = date_utils.end_of(today_date, "month") + relativedelta(months=- 1)
                leads = self.search([('company_id', '=', self.env.company.id), ('user_id', '=', self.env.user.id),
                                     ('type', '=', 'lead'), ('create_date', '>=', from_date),
                                     ('create_date', '<=', to_date)], order='create_date')
        month_start_lst = []
        month_lst = []
        count_lst = []
        table_value = []
        for rec in leads:
            if calendar.month_name[rec.create_date.month] not in month_lst:
                month_lst.append(calendar.month_name[rec.create_date.month])
                month_start_lst.append(date_utils.start_of(rec.create_date, "month").date())
        for i in range(0, len(month_lst)):
            count_lst.append(0)
            for rec in leads:
                if month_lst[i] == calendar.month_name[rec.create_date.month]:
                    count_lst[i] += 1

        for i in range(0, len(month_lst)):
            table_value.append({
                'month_start' : month_start_lst[i],
                'month': month_lst[i],
                'count': count_lst[i]
            })

        return {
            'table_value': table_value
        }

    @api.model
    def calculate_start_and_end_dates(self, selected_period):
        today_date = fields.date.today()
        from_date = today_date
        to_date = today_date
        if selected_period == 'this_year':
            from_date = date_utils.start_of(today_date, "year")
            to_date = date_utils.end_of(today_date, "year")
        elif selected_period == 'this_quater':
            from_date = self.calculate_quater()
            to_date = from_date + relativedelta(months=+ 3)
        elif selected_period == 'this_month':
            from_date = date_utils.start_of(today_date, "month")
            to_date = date_utils.end_of(today_date, "month")
        elif selected_period == 'this_week':
            from_date = date_utils.start_of(today_date, "week")
            to_date = date_utils.end_of(today_date, "week")

        return {
            'from_date': from_date,
            'to_date': to_date,
        }

    def demo(self):
        return 'hi','bye'

    @api.model
    def calculate_clicked_table_row_domain(self, isManager, selected_row_start_date):
        from_date = datetime.datetime.strptime(selected_row_start_date, '%Y-%m-%d').date()
        to_date = date_utils.end_of(from_date, "month")

        return{
            'from_date':from_date,
            'to_date':to_date
        }

# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AccessManager(models.Model):
    _name = 'access.manager'
    _description = 'Access Manger'
    _inherit = 'mail.thread'

    name = fields.Char(required=True)
    company_ids = fields.Many2many('res.company')
    user_profile_ids = fields.Many2many('user.profile')
    menu_ids = fields.Many2many('ir.ui.menu')
    hide_buttons_tab_ids = fields.One2many('hide.buttons.tab', 'access_manager_id')
    is_debug = fields.Boolean()
    is_chatter = fields.Boolean()
    field_access_ids = fields.One2many('field.access', 'access_manager_id')

    def hide_menus(self):
        """to hide menus"""
        for rec in self.menu_ids:
            for groups in rec.groups_id:
                for records in self.user_profile_ids:
                    for profile_groups in records.group_ids:
                        if groups.id == profile_groups.id:
                            rec.groups_id = [fields.Command.unlink(groups.id)]

    @api.model
    def check_user_for_debug(self):
        """to restrict debug mode for groups in profile"""
        access_records = self.search([('is_debug', '=', True)])
        for access in access_records:
            if access.company_ids:
                if self.env.company.id in access.company_ids.ids:
                    for rec in access.user_profile_ids:
                        for records in rec.group_ids:
                            if self.env.user.id in records.users.ids:
                                return True
            else:
                for rec in access.user_profile_ids:
                    for records in rec.group_ids:
                        if self.env.user.id in records.users.ids:
                            return True

    @api.model
    def check_user_for_chatter(self):
        """to hide chatter for groups in profile"""
        access_records = self.search([('is_chatter', '=', True)])
        for access in access_records:
            if access.company_ids:
                if self.env.company.id in access.company_ids.ids:
                    for rec in access.user_profile_ids:
                        for records in rec.group_ids:
                            if self.env.user.id in records.users.ids:
                                return True
            else:
                for rec in access.user_profile_ids:
                    for records in rec.group_ids:
                        if self.env.user.id in records.users.ids:
                            return True

    @api.model
    def hide_buttons_tab(self,model):
        """to hide button and tab for groups in profile"""
        button = {}
        tab = {}
        button_string = []
        button_name = []
        tab_string = []
        for records in self.env['hide.buttons.tab'].search([('model_id.model', '=', model)]):
            for access in records.access_manager_id:
                if access.company_ids:
                    if self.env.company.id in access.company_ids.ids:
                        for profile in access.user_profile_ids:
                            for group in profile.group_ids:
                                if self.env.user.id in group.users.ids:
                                    for rec in records.button_ids:
                                        button_string.append(rec.string)
                                        button_name.append(rec.method)
                                    for rec in records.tab_ids:
                                        tab_string.append(rec.name)
                else:
                    for profile in access.user_profile_ids:
                        for group in profile.group_ids:
                            if self.env.user.id in group.users.ids:
                                for rec in records.button_ids:
                                    button_string.append(rec.string)
                                    button_name.append(rec.method)
                                for rec in records.tab_ids:
                                    tab_string.append(rec.name)

        button['button_string'] = button_string
        button['button_name'] = button_name
        tab['tab_string'] = tab_string

        return {
            'button':button,
            'tab':tab,
        }

    @api.model
    def field_hide(self,model):
        field_hide = []
        field_readonly = []
        for records in self.env['field.access'].search([('model_id.model', '=', model)]):
            for access in records.access_manager_id:
                if access.company_ids:
                    if self.env.company.id in access.company_ids.ids:
                        for profile in access.user_profile_ids:
                            for group in profile.group_ids:
                                if self.env.user.id in group.users.ids:
                                    if records._is_invisible:
                                        for rec in records.field_ids:
                                            field_hide.append(rec.name)
                                    if records._is_readonly:
                                        for rec in records.field_ids:
                                            field_readonly.append(rec.name)

                else:
                    for profile in access.user_profile_ids:
                        for group in profile.group_ids:
                            if self.env.user.id in group.users.ids:
                                if records._is_invisible:
                                    for rec in records.field_ids:
                                        field_hide.append(rec.name)
                                if records._is_readonly:
                                    for rec in records.field_ids:
                                        field_readonly.append(rec.name)
        return {
            'field_hide':field_hide,
            'field_readonly':field_readonly,
        }



    def action_apply_changes(self):
        print('hi')
        # self.hide_menus()
        # self.check_user_for_chatter()


# -*- coding: utf-8 -*-
from odoo import api,fields,models
from bs4 import BeautifulSoup


class AccessManager(models.Model):
    _name = 'access.manager'

    name = fields.Char(required=True)
    company_ids = fields.Many2many('res.company')
    user_profile_ids = fields.Many2many('user.profile')
    menu_ids = fields.Many2many('ir.ui.menu')
    hide_buttons_tab_ids = fields.One2many('hide.buttons.tab','access_manager_id')


    def hide_menus(self):
        for rec in self.menu_ids:
            for groups in rec.groups_id:
                for records in self.user_profile_ids:
                    for profile_groups in records.group_ids:
                        if groups.id == profile_groups.id:
                            rec.groups_id = [fields.Command.unlink(groups.id)]


    def hide_buttons(self):
        records = self.env['ir.ui.view'].search([('id', '=', 4)])
        result = BeautifulSoup(records.arch_db)
        buttons = result.find_all('button')
        selection_field = []
        for i in buttons:
            values = i.attrs
            selection_value = f"{values['string']} ({values['name']})"
            selection_key = values['name']
            selection_field.append((selection_key,selection_value))
        print(selection_field)

    def action_apply_changes(self):
        print('hi')
        # self.hide_menus()
        # self.hide_buttons()
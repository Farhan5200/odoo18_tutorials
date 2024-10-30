# -*- coding: utf-8 -*-

from odoo import api,fields,models

class AccessManager(models.Model):
    _name = 'access.manager'

    name = fields.Char(required=True)
    company_ids = fields.Many2many('res.company')
    user_profile_ids = fields.Many2many('user.profile')
    menu_ids = fields.Many2many('ir.ui.menu')


    def hide_menus(self):
        for rec in self.menu_ids:
            for groups in rec.groups_id:
                for records in self.user_profile_ids:
                    for profile_groups in records.group_ids:
                        if groups.id == profile_groups.id:
                            rec.groups_id = [fields.Command.unlink(groups.id)]
                    # print(rec.groups_id)


    def action_apply_changes(self):
        self.hide_menus()
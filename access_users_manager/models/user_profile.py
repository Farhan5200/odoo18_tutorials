# -*- coding: utf-8 -*-

from odoo import api,fields,models

class UserProfile(models.Model):
    _name = 'user.profile'
    _description = 'User Profile'

    name = fields.Char()
    user_ids = fields.Many2many('res.users')
    color = fields.Integer(string="Color")
    group_ids = fields.Many2many('res.groups')


    # @api.onchange('group_ids','user_ids')
    # def add_users_to_group(self):
    #     for rec in self.group_ids:
    #         print(rec)
    #         rec.users += self.user_ids

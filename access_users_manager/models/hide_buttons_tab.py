# -*- coding: utf-8 -*-

from odoo import api,fields,models
from bs4 import BeautifulSoup


class HideButtonsTab(models.Model):
    _name = 'hide.buttons.tab'

    model_id = fields.Many2one('ir.model')
    buttons = fields.Selection(selection='_compute_button_selection', depends='m')

    @api.depends('m')
    def _compute_button_selection(self):
        records = self.env['ir.ui.view'].search([('model', '=', self.model_id.model)])
        selection_field = [('e','e')]
        for rec in records:
            result = BeautifulSoup(rec.arch_db)
            buttons = result.find_all('button')
            if buttons:
                for i in buttons:
                    values = i.attrs
                    if 'name' in values.keys() and 'string' in values.keys():
                        selection_value = f"{values['string']} ({values['name']})"
                        selection_key = values['name']
                        selection_field.append((selection_key,selection_value))
        print(selection_field)
        return selection_field

    access_manager_id = fields.Many2one('access.manager')

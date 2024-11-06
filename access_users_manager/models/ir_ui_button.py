# -*- coding: utf-8 -*-

from odoo import api, fields, models
from bs4 import BeautifulSoup


class IrUiButton(models.Model):
    """records of buttons in all views"""
    _name = 'ir.ui.button'
    _description = 'Ir Ui Button'

    name = fields.Char(required=True)
    string = fields.Char()
    type = fields.Selection([('object', 'Object'), ('action', 'Action')])
    method = fields.Char()
    model = fields.Char()
    view_id = fields.Many2one('ir.ui.view')

    @api.model
    def data_creation(self):
        """works while installing the module to create button datas"""
        records = self.env['ir.ui.view'].search([])
        for rec in records:
            result = BeautifulSoup(rec.arch_db)
            buttons = result.find_all('button')
            if buttons:
                for i in buttons:
                    values = i.attrs
                    if 'name' in values.keys() and 'string' in values.keys() and 'type' in values.keys():
                        self.env['ir.ui.button'].create({
                            'name': f"{values['string']} ({values['name']})",
                            'string': values['string'],
                            'method': values['name'],
                            'type': values['type'],
                            'model': rec.model,
                            'view_id': rec.id,
                        })

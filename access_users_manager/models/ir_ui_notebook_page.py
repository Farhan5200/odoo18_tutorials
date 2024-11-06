# -*- coding: utf-8 -*-

from odoo import api,fields,models
from bs4 import BeautifulSoup


class IrUiNotebookPage(models.Model):
    """records of notebook page in all views"""
    _name = 'ir.ui.notebook.page'
    _description = 'Ir Ui Notebook Page'

    name = fields.Char(required=True)
    model = fields.Char()
    view_id = fields.Many2one('ir.ui.view')

    @api.model
    def data_creation(self):
        """works while installing the module to create page datas"""
        records = self.env['ir.ui.view'].search([])
        for rec in records:
            result = BeautifulSoup(rec.arch_db)
            notebook = result.find_all('page')
            if notebook:
                for i in notebook:
                    values = i.attrs
                    if 'string' in values.keys():
                        self.env['ir.ui.notebook.page'].create({
                            'name': values['string'],
                            'model': rec.model,
                            'view_id': rec.id,
                        })

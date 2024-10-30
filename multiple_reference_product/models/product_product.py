# -*- coding: utf-8 -*-

from odoo import models

class ProductProduct(models.Model):
    _inherit = 'product.product'

    def action_show_more(self):
        """to show all of its references"""
        return{
            'name': f'{self.name} References',
            'type': 'ir.actions.act_window',
            'res_model': 'multiple.reference.product',
            'view_mode': 'list,form',
            'view_type': 'form',
            'domain': [("product_id", "=", self.id)],
            'context': {'default_product_id': self.id,'create': True},
            'target': 'current',
        }

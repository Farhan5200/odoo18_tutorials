# -*- coding: utf-8 -*-

from odoo import fields,models

class MultipleReferenceProduct(models.Model):
    """to add multiple references to a product"""
    _name = 'multiple.reference.product'


    name = fields.Char(required=True)
    product_id = fields.Many2one('product.product')


    def set_default_code(self):
        """to set the selected code as default"""
        for rec in self:
            rec.product_id.default_code = rec.name
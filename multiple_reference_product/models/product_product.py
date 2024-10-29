# -*- coding: utf-8 -*-

from odoo import fields,models

class ProductProduct(models.Model):
    _inherit = 'product.product'

    multiple_reference_ids = fields.One2many('multiple.reference.product','product_id')

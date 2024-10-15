# -*- coding: utf-8 -*-

from odoo import api,fields,models

class SaleOrderLine(models.Model):
    """to create dynamic domain"""
    _inherit = 'sale.order.line'


    ordered_product_ids = fields.Many2many('product.template',compute='_compute_order_products')

    @api.depends('order_id')
    def _compute_order_products(self):
        """function for dynamic domain"""
        for rec in self:
            if rec.order_id.partner_id.is_only_ordered:
                rec.ordered_product_ids = rec.env['product.template'].search([('invoice_policy', '=', 'order'),('sale_ok', '=', True)])
            else:
                rec.ordered_product_ids = rec.env['product.template'].search([('sale_ok', '=', True)])

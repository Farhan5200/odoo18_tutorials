# -*- coding: utf-8 -*-

from odoo import fields,models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        """to create invoice for those who enabled is_only_ordered"""
        super().action_confirm()
        if self.partner_id.is_only_ordered:
            created_invoice = self._create_invoices()
            created_invoice.action_post()

# -*- coding: utf-8 -*-

from odoo import fields,models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        """to change state of the lead to sate mentioned inside sales team"""
        super().action_confirm()
        if self.team_id.lead_stage and self.team_id.lead_stage != self.opportunity_id.stage_id:
            self.opportunity_id.stage_id = self.team_id.lead_stage

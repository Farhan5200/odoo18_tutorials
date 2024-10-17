# -*- coding: utf-8 -*-

from odoo import api, fields, models

class CrmTeam(models.Model):
    """to add a new field inside sales team"""
    _inherit = 'crm.team'

    lead_stage = fields.Many2one('crm.stage')
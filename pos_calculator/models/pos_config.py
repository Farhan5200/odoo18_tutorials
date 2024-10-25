# -*- coding: utf-8 -*-

from odoo import fields,models

class PosConfig(models.Model):
    """to add field's in pos settings"""
    _inherit = 'pos.config'

    pos_virtual_calculator = fields.Boolean(string="Virtual Calculator")

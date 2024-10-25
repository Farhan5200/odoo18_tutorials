# -*- coding: utf-8 -*-

from odoo import fields,models

class ResConfigSettings(models.TransientModel):
    """to add field's in settings"""
    _inherit = "res.config.settings"

    Virtual_calculator = fields.Boolean(string="Virtual Calculator", related="pos_config_id.pos_virtual_calculator", readonly=False)

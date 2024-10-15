# -*- coding: utf-8 -*-

from odoo import fields,models

class ResPartner(models.Model):
    """to add a field in contact"""
    _inherit = 'res.partner'

    is_only_ordered = fields.Boolean()

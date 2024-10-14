# -*- coding: utf-8 -*-

from odoo import fields,models

class UtmMedium(models.Model):
    _inherit = 'utm.medium'

    color = fields.Integer()
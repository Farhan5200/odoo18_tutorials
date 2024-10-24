# -*- coding: utf-8 -*-

from odoo import fields,models

class SurveySurvey(models.Model):
    """to add new one2many field for contact creation"""
    _inherit = 'survey.survey'

    survey_contact_ids = fields.One2many('survey.contact', 'survey_id')

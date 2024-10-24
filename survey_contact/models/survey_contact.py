# -*- coding: utf-8 -*-

from odoo import fields,models

class SurveyContact(models.Model):
    """to select questions to create contact"""
    _name = 'survey.contact'
    _description = 'Create Contact From Survey'

    survey_id = fields.Many2one('survey.survey')
    question_id = fields.Many2one('survey.question', domain="[('survey_id', '=', survey_id)]", required=True)
    partner_field_select = fields.Many2one('ir.model.fields', domain="[('model_id.model', '=', 'res.partner')]")

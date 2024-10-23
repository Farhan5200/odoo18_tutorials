# -*- coding: utf-8 -*-
from pkg_resources import require

from odoo import api,fields,models

class SurveyContact(models.Model):
    _name = 'survey.contact'
    _description = 'Create Contact From Survey'

    def partner_fields(self):
        selections_values = []
        for field,label in self.env['res.partner'].fields_get().items():
            selections_values.append((field,label['string']))
        return selections_values

    survey_id = fields.Many2one('survey.survey')
    question_id = fields.Many2one('survey.question', domain="[('survey_id', '=', survey_id)]", required=True)
    partner_field_select  =fields.Selection(partner_fields,string='Contact Field', required=True)


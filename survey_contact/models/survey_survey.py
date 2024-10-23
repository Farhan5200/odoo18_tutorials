# -*- coding: utf-8 -*-

from odoo import fields,models

class SurveySurvey(models.Model):
    _inherit = 'survey.survey'

    survey_contact_ids = fields.One2many('survey.contact', 'survey_id')

    def demo(self):
        print('hi')
        print(self.env['res.partner'].fields_get())
        for i,j in self.env['res.partner'].fields_get().items():
            print(j['string'])

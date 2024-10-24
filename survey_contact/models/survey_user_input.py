# -*- coding: utf-8 -*-

from odoo import models

class SurveyUserInput(models.Model):
    """to super the mark done function"""
    _inherit = 'survey.user_input'


    def _mark_done(self):
        """to add lines to create contact"""
        res = super()._mark_done()
        contact_create_values = {}
        for records in self.survey_id.survey_contact_ids:
            answer_details = self.user_input_line_ids.filtered(lambda r: r.question_id == records.question_id).read()
            answer_type = f'value_{answer_details[0]["answer_type"]}'
            contact_create_values[records.partner_field_select_id.name] = answer_details[0][answer_type]
        self.env['res.partner'].create(contact_create_values)
        return res

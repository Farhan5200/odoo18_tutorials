# -*- coding: utf-8 -*-

from odoo import models

class SurveyUserInput(models.Model):
    """to super the mark done function"""
    _inherit = 'survey.user_input'


    def _mark_done(self):
        """to add lines to create contact"""
        res = super()._mark_done()
        contact_create_values = {}
        if self.survey_id.survey_contact_ids:
            for records in self.survey_id.survey_contact_ids:
                for rec in self.user_input_line_ids:
                    if rec.question_id == records.question_id:
                        if rec.answer_type == 'text_box':
                            contact_create_values[records.partner_field_select.name] = rec.value_text_box
                        if rec.answer_type == 'char_box':
                            contact_create_values[records.partner_field_select.name] = rec.value_char_box
                        if rec.answer_type == 'numerical_box':
                            contact_create_values[records.partner_field_select.name] = rec.value_numerical_box
                        if rec.answer_type == 'scale':
                            contact_create_values[records.partner_field_select.name] = rec.value_scale
                        if rec.answer_type == 'date':
                            contact_create_values[records.partner_field_select.name] = rec.value_date
                        if rec.answer_type == 'datetime':
                            contact_create_values[records.partner_field_select.name] = rec.value_datetime
            self.env['res.partner'].create(contact_create_values)
        return res


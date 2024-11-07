# -*- coding: utf-8 -*-

from odoo import api, fields, models

class FieldAccess(models.Model):
    _name = 'field.access'
    _description = 'Field Access'


    model_id = fields.Many2one('ir.model')
    field_ids = fields.Many2many('ir.model.fields',required=True)
    access_manager_id = fields.Many2one('access.manager')
    dynamic_field_ids = fields.Many2many('ir.model.fields', compute='_compute_field_ids')
    _is_invisible = fields.Boolean()
    _is_readonly = fields.Boolean()
    _is_external_link = fields.Boolean()

    @api.depends('model_id')
    def _compute_field_ids(self):
        """function for dynamic domain of fields"""
        for rec in self:
            rec.dynamic_field_ids = rec.env['ir.model.fields'].search([('model_id.id', '=', rec.model_id.id)])

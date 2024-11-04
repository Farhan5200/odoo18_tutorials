# -*- coding: utf-8 -*-

from odoo import api,fields,models


class HideButtonsTab(models.Model):
    _name = 'hide.buttons.tab'

    model_id = fields.Many2one('ir.model')
    button_id = fields.Many2one('ir.ui.button')
    button_ids = fields.Many2many('ir.ui.button', compute="_compute_model_buttons")
    access_manager_id = fields.Many2one('access.manager')

    @api.depends('model_id')
    def _compute_model_buttons(self):
        """function for dynamic domain"""
        for rec in self:
            rec.button_ids = rec.env['ir.ui.button'].search([('model', '=', rec.model_id.model)])

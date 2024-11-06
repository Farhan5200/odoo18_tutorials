# -*- coding: utf-8 -*-

from odoo import api,fields,models


class HideButtonsTab(models.Model):
    """model which stores records of button and tab that need to be hidden using for one2many in access manager"""
    _name = 'hide.buttons.tab'
    _description = 'Hide Button Tab'

    model_id = fields.Many2one('ir.model')
    button_ids = fields.Many2many('ir.ui.button')
    button_dynamic_ids = fields.Many2many('ir.ui.button', compute="_compute_model_buttons")
    tab_ids = fields.Many2many('ir.ui.notebook.page')
    tab_dynamic_ids = fields.Many2many('ir.ui.notebook.page', compute="_compute_model_page")
    access_manager_id = fields.Many2one('access.manager')

    @api.depends('model_id')
    def _compute_model_buttons(self):
        """function for dynamic domain of buttons"""
        for rec in self:
            rec.button_dynamic_ids = rec.env['ir.ui.button'].search([('model', '=', rec.model_id.model)])

    @api.depends('model_id')
    def _compute_model_page(self):
        """function for dynamic domain of tabs"""
        for rec in self:
            rec.tab_dynamic_ids = rec.env['ir.ui.notebook.page'].search([('model', '=', rec.model_id.model)])

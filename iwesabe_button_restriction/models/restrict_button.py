# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class RestrictButton(models.Model):
    _name = 'restrict.button'
    _description = "Restrict Button"
    _rec_name = "display_name"

    display_name = fields.Char('', compute="compute_display_name")
    button_name = fields.Char('Button Name')
    button_type = fields.Selection([('object','Object'),('action','Action')], default='object')
    ir_model_id = fields.Many2one('ir.model', string="Model")
    user_ids = fields.Many2many('res.users','restrict_btn_user_ids','btn_id','user_ids', string="Restrict User(s)")
    validation_msg = fields.Text('', default="""You've no access to do this operation.\n Please Contact your administrator.""")
    
    @api.depends('button_name','button_type','ir_model_id')
    def compute_display_name(self):
        for record in self:
            display_name = "NEW"
            if record.ir_model_id and record.button_name:
                display_name = record.ir_model_id.name + ' - '+ record.button_name
            record.display_name = display_name

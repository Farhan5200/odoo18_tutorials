# -*- coding: utf-8 -*-

from odoo import models, api, fields, tools,_
from odoo.exceptions import UserError


class IrActionsActWindow(models.Model):
	_inherit = 'ir.actions.act_window'

	def read(self, fields=None, load='_classic_read'):
		self.clear_caches()
		domain = [('button_name','=',str(self.id)),('button_type','=','action')]
		active_model = self._context.get('active_model')
		if active_model:
			domain += [('ir_model_id.model','=',active_model)]
			restrict_button_record_ids = self.env['restrict.button'].sudo().search(domain)
			if restrict_button_record_ids:
				UserRestrict = restrict_button_record_ids.filtered(lambda x:self.env.user.id in x.user_ids.ids)
				if UserRestrict:
					raise UserError(_(UserRestrict[0].validation_msg))
		result = super().read(fields,load)
		return result
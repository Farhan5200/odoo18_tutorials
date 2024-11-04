# -*- coding: utf-8 -*-

from odoo import http, _
from odoo.http import request
from odoo.addons.web.controllers.dataset import DataSet
from odoo.exceptions import UserError

class IwesabeDataSet(DataSet):

	@http.route('/web/dataset/call_button', type='json', auth="user")
	def call_button(self, model, method, args, kwargs):
		restrict_button_record_ids = request.env['restrict.button'].sudo().search([('ir_model_id.model','=',model),('button_name','=',method),('button_type','=','object')])
		if restrict_button_record_ids:
			UserRestrict = restrict_button_record_ids.filtered(lambda x:request.env.user.id in x.user_ids.ids)
			if UserRestrict:
				raise UserError(_(UserRestrict[0].validation_msg))
		result = super().call_button(model, method, args, kwargs)
		return result
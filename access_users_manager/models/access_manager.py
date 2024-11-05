# -*- coding: utf-8 -*-
from odoo import api,fields,models
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup


class AccessManager(models.Model):
    _name = 'access.manager'
    _inherit = 'mail.thread'

    name = fields.Char(required=True)
    company_ids = fields.Many2many('res.company')
    user_profile_ids = fields.Many2many('user.profile')
    menu_ids = fields.Many2many('ir.ui.menu')
    hide_buttons_tab_ids = fields.One2many('hide.buttons.tab','access_manager_id')
    is_debug = fields.Boolean()
    is_chatter = fields.Boolean()


    def hide_menus(self):
        for rec in self.menu_ids:
            for groups in rec.groups_id:
                for records in self.user_profile_ids:
                    for profile_groups in records.group_ids:
                        if groups.id == profile_groups.id:
                            rec.groups_id = [fields.Command.unlink(groups.id)]


    # def hide_buttons(self):
    #     root = ET.fromstring(self.hide_buttons_tab_ids.button_id.view_id.arch_db)
    #     tree = ET.ElementTree(root).getroot()
    #     for i in ET.fromstring(self.hide_buttons_tab_ids.button_id.view_id.arch_db).iter('button'):
    #         if i.attrib['name'] == 'action_create_invoice':
    #             i.set('invisible','1')
    #             modified_xml_string = ET.tostring(i, encoding='UTF-8')
    #             print(self.hide_buttons_tab_ids.button_id.view_id.arch_db)

    @api.model
    def check_user_for_debug(self):
        access_records = self.search([('is_debug', '=', True)])
        for access in access_records:
            for rec in access.user_profile_ids:
                for records in rec.group_ids:
                    if self.env.user.id in records.users.ids:
                        return True

    @api.model
    def check_user_for_chatter(self):
        print('kkijiiji')
        access_records = self.search([('is_chatter', '=', True)])
        for access in access_records:
            for rec in access.user_profile_ids:
                for records in rec.group_ids:
                    if self.env.user.id in records.users.ids:
                        print('vcuuu')
                        return True

    def action_apply_changes(self):
        print('hi')
        # self.hide_menus()
        # self.hide_buttons()

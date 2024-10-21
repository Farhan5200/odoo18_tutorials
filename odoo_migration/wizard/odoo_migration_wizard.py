# -*- coding: utf-8 -*-

from odoo import fields,models
import xmlrpc.client

class OdooMigrationWizard(models.Model):
    _name = 'odoo.migration.wizard'
    _description = 'Odoo Migration Wizard'


    def migrate_odoo(self):
        url_db1 = "http://localhost:8016/"
        db_1 = 'latest_db'
        username_db_1 = 'admin'
        password_db_1 = 'admin'
        common_1 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url_db1))
        models_1 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url_db1))
        # version_db1 = common_1.version()

        # url_db2 = "http://cybrosys:8017/"
        # db_2 = 'odoo17-18_migration'
        # username_db_2 = 'admin'
        # password_db_2 = 'admin'
        # common_2 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url_db2))
        # models_2 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url_db2))
        # version_db2 = common_2.version()

        uid_db1 = common_1.authenticate(db_1, username_db_1, password_db_1, {})
        # uid_db2 = common_2.authenticate(db_2, username_db_2, password_db_2, {})
        #
        db_1_contacts = models_1.execute_kw(db_1, uid_db1, password_db_1, 'res.partner', 'search_read', [],
                                         {'fields': ['name', 'email', 'id']})

        for partner in db_1_contacts:
            if self.env['res.partner'].search([('id', '=', partner['id'])]):
                pass
            else:
                self.env['res.partner'].create({
                    'id': partner['id'],
                    'name': partner['name'],
                    'email': partner['email'],
                })





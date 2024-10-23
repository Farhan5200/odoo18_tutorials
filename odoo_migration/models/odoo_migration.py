# -*- coding: utf-8 -*-

from odoo import api, models
import xmlrpc.client


class OdooMigrationWizard(models.TransientModel):
    """to migrate purchase orders"""
    _name = 'odoo.migration'
    _description = 'Odoo Migration'

    @api.model
    def migrate_odoo(self,url_db1,db_1,username_db_1,password_db_1,url_db2,db_2,username_db_2,password_db_2):
        """to migrate purchase orders"""
        # url_db1 = "http://localhost:8016/"
        # db_1 = 'test_migrate_17'
        # username_db_1 = 'admin'
        # password_db_1 = 'admin'

        # url_db2 = "http://cybrosys:8017/"
        # db_2 = 'odoo17-18_migration'
        # username_db_2 = 'admin'
        # password_db_2 = 'admin'

        try:
            common_1 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url_db1))
            models_1 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url_db1))
            common_2 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url_db2))
            models_2 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url_db2))

            uid_db1 = common_1.authenticate(db_1, username_db_1, password_db_1, {})
            uid_db2 = common_2.authenticate(db_2, username_db_2, password_db_2, {})

            db_1_contacts = models_1.execute_kw(db_1, uid_db1, password_db_1, 'res.partner', 'search_read', [],
                                                {'fields': ['name', 'email', 'id', 'customer_rank', 'supplier_rank']})
            testing_con = models_2.execute_kw(db_2, uid_db2, password_db_2, 'res.partner', 'search_read', [],
                                   {'fields': ['name']})
        except:

            return False

        """to create contacts"""
        for partner in db_1_contacts:
            if models_2.execute_kw(db_2, uid_db2, password_db_2, 'res.partner', 'search', [],
                                   {'domain': [('name', '=', partner['name'])]}):
                pass
            else:
                models_2.execute_kw(db_2, uid_db2, password_db_2, 'res.partner', 'create', [{
                    'id': partner['id'],
                    'name': partner['name'],
                    'email': partner['email'],
                    'customer_rank': partner['customer_rank'],
                    'supplier_rank': partner['supplier_rank']
                }])

        db_1_products = models_1.execute_kw(db_1, uid_db1, password_db_1, 'product.template', 'search_read', [],
                                            {'fields': ['name', 'id', 'sale_ok', 'invoice_policy', 'purchase_ok',
                                                        'list_price', 'standard_price', 'default_code']})
        """to create products"""
        for products in db_1_products:
            models_2.execute_kw(db_2, uid_db2, password_db_2, 'product.template', 'create', [{
                'id': products['id'],
                'name': products['name'],
                'default_code': products['default_code'],
                'sale_ok': products['sale_ok'],
                'invoice_policy': products['invoice_policy'],
                'purchase_ok': products['purchase_ok'],
                'list_price': products['list_price'],
                'standard_price': products['standard_price'],
            }])

        db_1_purchase_order = models_1.execute_kw(db_1, uid_db1, password_db_1, 'purchase.order', 'search_read', [],
                                                  {'domain': [('state', '=', 'purchase')]})

        db_1_purchase_order_line = models_1.execute_kw(db_1, uid_db1, password_db_1, 'purchase.order.line',
                                                       'search_read', [],
                                                       {'domain': [('order_id.state', '=', 'purchase')]})
        """to create purchase order"""
        for i in db_1_purchase_order:
            partner = models_2.execute_kw(db_2, uid_db2, password_db_2, 'res.partner', 'search_read', [], {
                'domain': [('name', '=', i['partner_id'][1])]
            })
            purchase_order_id = models_2.execute_kw(db_2, uid_db2, password_db_2, 'purchase.order', 'create', [{
                'partner_id': partner[0]['id'],
                'date_order': i['date_order'],
                'amount_total': i['amount_total'],
                'state': i['state'],
                'date_approve': i['date_approve'],
                'date_planned': i['date_planned'],
                'currency_id': i['currency_id'][0]
            }])
            for j in db_1_purchase_order_line:
                if i['id'] == j['order_id'][0]:
                    prod_name = j['product_id'][1]
                    for str in prod_name:
                        if str == ']':
                            prod_name = prod_name.strip(str)
                            break
                        else:
                            prod_name = prod_name.strip(str)
                    prod_name = prod_name.lstrip(' ')
                    product = models_2.execute_kw(db_2, uid_db2, password_db_2, 'product.template', 'search_read', [], {
                        'domain': [('name', '=', prod_name)]
                    })
                    models_2.execute_kw(db_2, uid_db2, password_db_2, 'purchase.order.line', 'create', [{
                        'name': prod_name,
                        'product_id': product[0]['id'],
                        'order_id': purchase_order_id,
                        'product_qty': j['product_qty'],
                        'price_unit': j['price_unit'],
                        'product_uom': j['product_uom'][0],
                        'display_type': j['display_type']
                    }])
        return True

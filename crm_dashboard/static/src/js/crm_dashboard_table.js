/** @odoo-module */

import PublicWidget from "@web/legacy/js/public/public_widget";
//import { jsonrpc } from "@web/core/network/rpc_service";

PublicWidget.registry.crmDashboardTable = PublicWidget.Widget.extend({
    selector: '.crm_dashboard_table',
    events:{
        'click .clicked_table_row_leads': '_onClick_clicked_table_row_leads',
    },

    _onClick_clicked_table_row_leads: function(){
        console.log('helloo guys')
    },
    });

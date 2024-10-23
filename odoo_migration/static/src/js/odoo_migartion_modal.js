/* @odoo-module */

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";


class Migration extends Component{
    setup(){
        this.orm = useService("orm");
        this.uiService = useService("ui");
        this.dialogService = useService("dialog");
        this.action = useService("action")
        this.effect = useService("effect");
    }

    async odoo_migrate(){
        var url_db1 = document.getElementById('url_db1').value
        var db_1 = document.getElementById('db_1').value
        var username_db_1 = document.getElementById('username_db_1').value
        var password_db_1 = document.getElementById('password_db_1').value

        var url_db2 = document.getElementById('url_db2').value
        var db_2 = document.getElementById('db_2').value
        var username_db_2 = document.getElementById('username_db_2').value
        var password_db_2 = document.getElementById('password_db_2').value

        this.uiService.block()
        const result =await this.orm.call('odoo.migration', 'migrate_odoo', [url_db1,db_1,username_db_1,password_db_1,url_db2,db_2,username_db_2,password_db_2])
        if (result){
            this.uiService.unblock()
            this.effect.add({
                        message: "Congratulations Migration Completed",
                        type: "rainbow_man",
                        fadeout: "fast",
                    });
            setTimeout(() => {
                this.action.doAction({
                type: 'ir.actions.client',
                tag: 'reload',
            });
            }, 2000);
        }
        else{
            this.uiService.unblock()
            this.dialogService.add(AlertDialog, {
                body:"Invalid Credentials",
            });
        }
    }
}

Migration.template = "odoo_migration.odoo_migration_modal"

registry.category("actions").add("odoo_migration_modal",Migration)

/* @odoo-module */

import { patch } from "@web/core/utils/patch";
import { MessagingMenu } from "@mail/core/public_web/messaging_menu";
import { useService } from "@web/core/utils/hooks";


patch(MessagingMenu.prototype, {
    setup() {
        super.setup()
        this.action = useService("action");
        },
    generate_qr(){
        console.log(this)
        this.action.doAction({
                type: 'ir.actions.client',
                tag: 'qr_generator_modal',
                target: "new",
            });
    }
});

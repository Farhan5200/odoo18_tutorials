/* @odoo-module */

import { patch } from "@web/core/utils/patch";
import { FormArchParser } from "@web/views/form/form_arch_parser";
import { useService } from "@web/core/utils/hooks";
import { jsonrpc } from "@web/core/network/rpc";
//import { onWillStart} from "@odoo/owl";



patch(FormArchParser.prototype, {
    //session will be logged out if user is not allowed to enter debug mode
    setup() {
        console.log('result')
//        this.orm = useService("orm");
//        onWillStart(async () => {
//            const result = await this.orm.call('access.manager','check_user_for_chatter', [],{});
//            console.log(result)
//            if (result){
//                alert('You are not allowed to enter debug mode please contact Administration')
//            }
//        });
//        return super.setup()
        },
        parse(xmlDoc, models, modelName){
        const result = super.parse(...arguments);
//            this.setup()
//            console.log(this,'ooolokoko')
            return result
        }
});

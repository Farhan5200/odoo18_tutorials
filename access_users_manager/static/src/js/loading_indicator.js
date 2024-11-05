/* @odoo-module */

import { patch } from "@web/core/utils/patch";
import { LoadingIndicator } from "@web/webclient/loading_indicator/loading_indicator";
import { useService } from "@web/core/utils/hooks";
import { onWillStart} from "@odoo/owl";



patch(LoadingIndicator.prototype, {
    //session will be logged out if user is not allowed to enter debug mode
    setup() {
        this.orm = useService("orm");
        if (odoo.debug){
            onWillStart(async () => {
                const result = await this.orm.call('access.manager','check_user_for_debug', [],{});
                if (result){
                    alert('You are not allowed to enter debug mode please contact Administration')
                    window.location.href = "/web/session/logout"
                }
            });
        }
        super.setup()
        },
});

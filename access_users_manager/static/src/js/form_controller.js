/* @odoo-module */

import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";
import { useService } from "@web/core/utils/hooks";
import { onWillStart} from "@odoo/owl";



patch(FormController.prototype, {
    setup() {
        const complete = super.setup()
            onWillStart(async () => {
                const result = await this.orm.call('access.manager','check_user_for_chatter', [],{});//returns weather chatter needs to be hidden or not
                if(result){
                    //hides chatter
                    this.archInfo.xmlDoc.querySelectorAll('chatter').forEach(function(i) {
                        i.setAttribute("invisible", "1")
                    });
                }
                const buttons_tab = await this.orm.call('access.manager','hide_buttons_tab', [this.props.resModel],{});//returns all the button and tab that need to be hidden
                //hides button
                this.archInfo.xmlDoc.querySelectorAll('button').forEach(function(i) {
                    if (i.attributes.string && i.attributes.name){
                        if(buttons_tab.button.button_string.includes(i.attributes.string.value) && buttons_tab.button.button_name.includes(i.attributes.name.value)){
                            i.setAttribute("invisible", "1")
                        }
                    }
                });
                //hides tab
                this.archInfo.xmlDoc.querySelectorAll('page').forEach(function(i) {
                    if (i.attributes.string){
                        if(buttons_tab.tab.tab_string.includes(i.attributes.string.value)){
                            i.setAttribute("invisible", "1")
                        }
                    }
                });
                //alter field
                const field_spec = await this.orm.call('access.manager','field_hide', [this.props.resModel],{});//returns all the fields that need to be hidden
                this.archInfo.xmlDoc.querySelectorAll('field').forEach(function(i) {
                    if (i.attributes.name){
                        if(field_spec.field_hide.includes(i.attributes.name.value)){
                            i.setAttribute("invisible", "1")
                        }
                        if(field_spec.field_readonly.includes(i.attributes.name.value)){
                            i.setAttribute("style","pointer-events: none;")
                        }
                    }
                });
            });
        return complete
    },
});

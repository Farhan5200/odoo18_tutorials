///* @odoo-module */
//
//import { patch } from "@web/core/utils/patch";
//import { Field } from "@web/views/fields/field";
//import { useService } from "@web/core/utils/hooks";
//import { onWillStart} from "@odoo/owl";
//
//
//
//patch(Field.prototype, {
//    setup() {
//        const completed = super.setup()
//        this.orm = useService("orm");
//        onWillStart(async () => {
//            const result = await this.orm.call('access.manager','fields_access', [this.props.record.model.config.resModel],{});
//
//        });
//        console.log('patched machuuuu')
//        return completed
//        },
//});

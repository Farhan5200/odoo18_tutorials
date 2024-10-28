/** @odoo-module */
import { PosCalculator } from "./pos_calculator_component";
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { patch } from "@web/core/utils/patch";
import { makeAwaitable } from "@point_of_sale/app/store/make_awaitable_dialog";


// to add new function to open calculator
patch(ControlButtons.prototype, {
    async openCalculator() {
         await makeAwaitable(this.dialog, PosCalculator, {
                title:'Calculator',
            });
    }
});

/** @odoo-module */
import { SelectionPopup } from "@point_of_sale/app/utils/input_popups/selection_popup";
import { PosCalculator } from "./pos_calculator_component";
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { patch } from "@web/core/utils/patch";
import { makeAwaitable } from "@point_of_sale/app/store/make_awaitable_dialog";


// to add new function to open calculator
patch(ControlButtons.prototype, {
    async openCalculator() {
         console.log(this)
         await makeAwaitable(this.dialog, PosCalculator, {
//         this.env.services.dialog.add(PosCalculator,{
                title:'New',
            });
//            const selectedProduct = await makeAwaitable(this.env.services.dialog, SelectionPopup, {
//                title: "Please select a product for this reward",
//                list: [('productsList','fff')],
//            });
    }
});

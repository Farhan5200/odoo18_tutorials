/** @odoo-module */
//import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";
import { Dialog } from "@web/core/dialog/dialog";

//import { useService } from "@web/core/utils/hooks";
//import { renderToFragment } from "@web/core/utils/render";


export class PosCalculator extends Component {
    static template = "pos_calculator.pos_calculator_modal";
    static components = { Dialog };
    static props = {
        title: { type: String, optional: true },
        close: Function,
        getPayload: Function,

    };
    static defaultProps = {
       title: "Customer Details",
    };
    computePayload() {
        const selected = this.props.list.find((item) => this.state.selectedId === item.id);
        return selected && selected.item;
    }
    confirm() {
        this.props.getPayload(this.computePayload());
        this.props.close();
    }
}

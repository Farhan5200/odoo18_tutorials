/** @odoo-module */
import { Component } from "@odoo/owl";
import { Dialog } from "@web/core/dialog/dialog";


export class PosCalculator extends Component {
    static template = "pos_calculator.pos_calculator_modal";
    static components = { Dialog };
    static props = {
        title: { type: String, optional: true },
        close: Function,
        getPayload: Function,

    };
    setup(){
    console.log(this.props)
    };
    static defaultProps = {
       title: "Calculator",
    };

    close() {
        this.props.close();
    }
    take_value(e){
        var ctx = document.getElementById('input_box').value
        ctx += e
        document.getElementById('input_box').value = ctx
    }
    calculate(){
        var ctx = document.getElementById('input_box').value
        try{
            ctx = eval(ctx)
        }
        catch(err){
            ctx = 'Syntax Error....'
        }
        document.getElementById('input_box').value = ctx
    }
    clear_all(){
        document.getElementById('input_box').value = ''
    }
    remove_last(){
        var ctx = document.getElementById('input_box').value
        ctx = ctx.slice(0, -1)
        console.log(ctx)
        document.getElementById('input_box').value = ctx
    }
}

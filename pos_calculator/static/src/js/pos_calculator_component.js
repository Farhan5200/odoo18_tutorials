/** @odoo-module */
import { Component } from "@odoo/owl";
import { Dialog } from "@web/core/dialog/dialog";


// calculator popup
export class PosCalculator extends Component {
    static template = "pos_calculator.pos_calculator_modal";
    static components = { Dialog };
    static props = {
        title: { type: String, optional: true },
        close: Function,
        getPayload: Function,

    };
    static defaultProps = {
       title: "Calculator",
    };

    close() {
    //to close the popup
        this.props.close();
    }
    take_value(e){
    //to take input
        var pattern = /\d*\.\d*$/
        // to check decimal point
        var ctx = document.getElementById('input_box').value
        if (e == '.'){
            var result= pattern.test(ctx)
            if(!result){
                ctx += e
            }
        }
        else{
            ctx += e
        }
        document.getElementById('input_box').value = ctx
    }
    calculate(){
    //to calculate
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
    //to clear all imput AC
        document.getElementById('input_box').value = ''
    }
    remove_last(){
    //to remove last input
        var ctx = document.getElementById('input_box').value
        ctx = ctx.slice(0, -1)
        console.log(ctx)
        document.getElementById('input_box').value = ctx
    }
}

/** @odoo-module */
import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { renderToFragment } from "@web/core/utils/render";


class QRCode extends Component {
    generate_qr(){
    //to generate qr code
        var text = $("#input_box").val()
        if (text){
            $('#qr_code').html(renderToFragment('qr_code_generator.qr_image', {
                text,
            }))
                $('#error').hide()
                $('#qr_code').show()
                $('#print_btn').show()
        }
        else{
            $('#error').show()
        }
    }
    reset_btn(){
    //while clicking reset button
        $('#input_box').val('')
        $('#qr_code').hide()
        $('#print_btn').hide()
    }
    async print_qr(){
    //while clicking save button
       const url = $($('#qr_img')[0].attributes.src).val()
       const image = await fetch(url)
       const imageBlog = await image.blob()
       const imageURL = URL.createObjectURL(imageBlog)
       const link = document.createElement('a')
       link.href = imageURL
       link.download = 'QR Code'
       document.body.appendChild(link)
       link.click()
       document.body.removeChild(link)
    }

}
QRCode.template = "qr_code_generator.qr_generator_modal"

registry.category("actions").add("qr_generator_modal",QRCode)

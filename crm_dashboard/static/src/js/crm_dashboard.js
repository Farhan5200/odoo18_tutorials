/**@odoo-module **/
import { registry } from "@web/core/registry";
import { Component } from  "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { onWillStart, useRef, onMounted } from "@odoo/owl";





const actionRegistry = registry.category("actions");
class CrmDashboard extends Component {
    setup() {
         this.orm = useService('orm')
         this.action = useService("action")
         this._fetch_data()
   }
   async _fetch_data(){
        const result =await this.orm.call('crm.lead','get_tiles_data',[],{})
        document.getElementById("my_lead").append(result.total_leads);
        document.getElementById("my_opportunity").append(result.total_opportunity);
        document.getElementById("templates_expected_revenue").append(result.currency + result.expected_revenue);
        document.getElementById("templates_revenue").append(result.currency + result.revenue);
        document.getElementById("templates_win_ratio").append(result.win_ratio);
        this.props.user_id = result.user_id
        this.props.company_id = result.company_id
        this.load_charts()
   }
   load_charts(){
   var ctx = document.getElementById('template_lost_dough')
        var chart = new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: [
                'Red',
                'Blue',
                'Yellow'
              ],
             datasets: [{
               backgroundColor:  [
                      'rgb(255, 99, 132)',
                      'rgb(54, 162, 235)',
                      'rgb(255, 205, 86)'
                    ],
                data: [20, 30, 40],
        }]
    },
    options: {
    }
    });
   }
   open_myLeads(){
        var company_id = this.props.company_id
        var user_id = this.props.user_id
        this.action.doAction({
                name:'My Leads',
                type: 'ir.actions.act_window',
                res_model: 'crm.lead',
                views: [[false, "list"]],
                view_mode: "list",
                domain:"[('company_id', '=', "+company_id+"),('user_id', '=', "+user_id+"),('type', '=', 'lead')]",
                target: "main",
            });
            console.log(this)
   }
   open_myOpportunity(){
        var company_id = this.props.company_id
        var user_id = this.props.user_id
        this.action.doAction({
                name:'My Opportunity',
                type: 'ir.actions.act_window',
                res_model: 'crm.lead',
                views: [[false, "list"]],
                view_mode: "list",
                domain:"[('company_id', '=', "+company_id+"),('user_id', '=', "+user_id+"),('type', '=', 'opportunity')]",
                target: "main",
            });
            console.log(this)
   }

}
CrmDashboard.template = "crm_dashboard.CrmDashboard";
actionRegistry.add("crm_dashboard_tag", CrmDashboard);

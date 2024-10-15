/**@odoo-module **/
import { registry } from "@web/core/registry";
import { Component } from  "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
//import { onWillStart, useRef, onMounted } from "@odoo/owl";





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
        this.load_doughnut_charts()
        this.load_pie_charts()
        this.load_doughnut_charts_campaign()
        this.load_bar_chart()
   }

   async load_doughnut_charts(){
   const result = await this.orm.call('crm.lead','doughnut_chart_values',[],{})
   var ctx = document.getElementById('template_doughnut')
        var chart = new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: result.medium_labels,
             datasets: [{
               backgroundColor:  [
                      'rgb(255, 99, 132)',
                      'rgb(54, 162, 235)',
                      'rgb(255, 205, 86)',
                      '#8fa0a8',
                      '#873e23',
                      '#151a13',
                      '#eab573',
                      '#1c416b',
                      '#69bdd2',
                      'rgb(223,200,162)'
                    ],
                data: result.medium_count,
        }]
    },
    });
   }

   async load_pie_charts(){
   const result = await this.orm.call('crm.lead','pie_chart_values',[],{})
   var ctx = document.getElementById('template_pie_chart')
        var chart = new Chart(ctx, {
        type: "pie",
        data: {
            labels: result.label_activity_type,
             datasets: [{
               backgroundColor:  [
                      'rgb(255, 99, 132)',
                      'rgb(54, 162, 235)',
                      'rgb(255, 205, 86)',
                      '#8fa0a8',
                      '#873e23',
                      '#151a13',
                      '#eab573',
                      '#1c416b',
                      '#69bdd2',
                      'rgb(223,200,162)'
                    ],
                data: result.label_activity_type_count,
        }]
    },
    });
   }

   async load_doughnut_charts_campaign(){
   const result = await this.orm.call('crm.lead','doughnut_chart_values_campaign',[],{})
   var ctx = document.getElementById('template_doughnut_campaign')
        var chart = new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: result.campaign_labels,
             datasets: [{
               backgroundColor:  [
                      'rgb(255, 99, 132)',
                      'rgb(54, 162, 235)',
                      'rgb(255, 205, 86)',
                      '#8fa0a8',
                      '#873e23',
                      '#151a13',
                      '#eab573',
                      '#1c416b',
                      '#69bdd2',
                      'rgb(223,200,162)'
                    ],
               data: result.campaign_count,
        }]
    },
    });
   }

   async load_bar_chart(){
        const result = await this.orm.call('crm.lead','bar_chart_values',[],{})
        var ctx = document.getElementById('template_bar_chart')
        var chart = new Chart(ctx, {
        type: "bar",
        data: {
            labels: ["Lead", "Opportunity"],
            datasets: [{
                backgroundColor: "red",
                label:'Lost',
                data: result.lost_count
            }]
        },
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
   }

}
CrmDashboard.template = "crm_dashboard.CrmDashboard";
actionRegistry.add("crm_dashboard_tag", CrmDashboard);

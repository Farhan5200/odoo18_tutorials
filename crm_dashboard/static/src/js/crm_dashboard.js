/**@odoo-module **/
import { registry } from "@web/core/registry";
import { Component } from  "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { user } from "@web/core/user";
import { useState } from "@odoo/owl";



const actionRegistry = registry.category("actions");
class CrmDashboard extends Component {
    setup() {
         this.orm = useService('orm')
         this.action = useService("action")
         this._fetch_data()
         this.load_table_values()
         this.state = useState({
            table_values : [],
         });
   }
   async _fetch_data(selected_period='all'){
        //to pass data to tiles
        this.isManager = await user.hasGroup("sales_team.group_sale_manager");
        const result =await this.orm.call('crm.lead','get_tiles_data',[selected_period,this.isManager],{})
        document.getElementById("my_lead").append(result.total_leads);
        document.getElementById("my_opportunity").append(result.total_opportunity);
        document.getElementById("templates_expected_revenue").append(result.currency + result.expected_revenue);
        document.getElementById("templates_revenue").append(result.currency + result.revenue);
        document.getElementById("templates_win_ratio").append(result.win_ratio);
        this.props.user_id = result.user_id
        this.props.company_id = result.company_id
        this.load_doughnut_charts(selected_period)
        this.load_pie_charts(selected_period)
        this.load_doughnut_charts_campaign(selected_period)
        this.load_bar_chart(selected_period)
   }

   selected_period(){
        var ctx = document.getElementById("selected_period")
        document.getElementById("my_lead").innerHTML = '';
        document.getElementById("my_opportunity").innerHTML = '';
        document.getElementById("templates_expected_revenue").innerHTML = '';
        document.getElementById("templates_revenue").innerHTML = '';
        document.getElementById("templates_win_ratio").innerHTML = '';
        this._fetch_data(ctx.value)
       }

   async load_doughnut_charts(selected_period){
   //to pass doughnet chart leads by medium values
   const result = await this.orm.call('crm.lead','doughnut_chart_values',[selected_period,this.isManager],{})
   var ctx = document.getElementById('template_doughnut')
   ctx.remove()
   document.getElementById('doughnut_chart').innerHTML = '<canvas id="template_doughnut"/>'
   ctx = document.getElementById('template_doughnut')
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

   async load_pie_charts(selected_period){
   //to pass pie chart activities values
   const result = await this.orm.call('crm.lead','pie_chart_values',[selected_period,this.isManager],{})
   var ctx = document.getElementById('template_pie_chart')
   ctx.remove()
   document.getElementById('pie_chart').innerHTML = '<canvas id="template_pie_chart"/>'
   ctx = document.getElementById('template_pie_chart')
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

   async load_doughnut_charts_campaign(selected_period){
   //to pass doughnet chart leads by campaign values
   const result = await this.orm.call('crm.lead','doughnut_chart_values_campaign',[selected_period, this.isManager],{})
   var ctx = document.getElementById('template_doughnut_campaign')
   ctx.remove()
   document.getElementById('doughnut_chart_campaign').innerHTML = '<canvas id="template_doughnut_campaign"/>'
   ctx = document.getElementById('template_doughnut_campaign')
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

   async load_bar_chart(selected_period){
   //to pass bar chart lost opportunity/lead values
        const result = await this.orm.call('crm.lead','bar_chart_values',[selected_period, this.isManager],{})
        var ctx = document.getElementById('template_bar_chart')
        ctx.remove()
        document.getElementById('bar_chart').innerHTML = '<canvas id="template_bar_chart" width="65rem" height="27rem" style="display: block; box-sizing: border-box;"/>'
        ctx = document.getElementById('template_bar_chart')
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

   async load_table_values(){
        //to pass table leads by month values
        this.isManager = await user.hasGroup("sales_team.group_sale_manager");
        var selected_option = 'all'
            const result = await this.orm.call('crm.lead','table_values',[this.isManager,selected_option],{})
        var ctx = document.getElementById('table_body')
        var i = 0
        this.state.table_values = result.table_value
   }

   async selected_period_lead_month_table(){
        var selected_option = document.getElementById('selected_period_lead_month').value
        const result = await this.orm.call('crm.lead','table_values',[this.isManager,selected_option],{})
        var ctx = document.getElementById('table_body')
        var i = 0
        this.state.table_values = result.table_value
   }

   async clicked_table_row(selected_row_start_date){
   //to open clicked row in table
        const result = await this.orm.call('crm.lead','calculate_clicked_table_row_domain',[this.isManager,selected_row_start_date],{})
        console.log(result.from_date)
        console.log(result.to_date)
        var company_id = this.props.company_id
        var user_id = this.props.user_id
        var created_domain = "[('company_id', '=', "+company_id+"),('type', '=', 'lead')]"
        if (this.isManager){
            created_domain = "[('company_id', '=', "+company_id+"),('type', '=', 'lead'),('create_date', '>=', '"+result.from_date+"'),('create_date', '<=', '"+result.to_date+"')]"
        }
        else{
            created_domain = "[('company_id', '=', "+company_id+"),('user_id', '=', "+user_id+"),('type', '=', 'lead'),('create_date', '>=', '"+result.from_date+"'),('create_date', '<=', '"+result.to_date+"')]"
        }
        this.action.doAction({
                name:'Leads',
                type: 'ir.actions.act_window',
                res_model: 'crm.lead',
                views: [[false, "list"]],
                view_mode: "list",
                domain: created_domain,
                target: "main",
            });
   }

   async open_myLeads(){
        //to open leads tile
        var ctx = document.getElementById("selected_period").value
        var company_id = this.props.company_id
        var user_id = this.props.user_id
        var created_domain = "[('company_id', '=', "+company_id+"),('type', '=', 'lead')]"
        const result = await this.orm.call('crm.lead','calculate_start_and_end_dates',[ctx],{})
        if (this.isManager){
            if (ctx == 'all'){
                created_domain = "[('company_id', '=', "+company_id+"),('type', '=', 'lead')]"
                }
            else{
                created_domain = "[('company_id', '=', "+company_id+"),('type', '=', 'lead'),('create_date', '>=', '"+result.from_date+"'),('create_date', '<=', '"+result.to_date+"')]"
            }
        }
        else{
            if (ctx == 'all'){
                created_domain = "[('company_id', '=', "+company_id+"),('user_id', '=', "+user_id+"),('type', '=', 'lead')]"
            }
            else{
                created_domain = "[('company_id', '=', "+company_id+"),('type', '=', 'lead'),('create_date', '>=', '"+result.from_date+"'),('create_date', '<=', '"+result.to_date+"'),('user_id', '=', "+user_id+")]"
            }
        }
        this.action.doAction({
                name:'Leads',
                type: 'ir.actions.act_window',
                res_model: 'crm.lead',
                views: [[false, "list"]],
                view_mode: "list",
                domain: created_domain,
                target: "main",
            });
   }

   async open_myOpportunity(){
        //to open opportunity tile
        var ctx = document.getElementById("selected_period").value
        var company_id = this.props.company_id
        var user_id = this.props.user_id
        var created_domain = "[('company_id', '=', "+company_id+"),('type', '=', 'opportunity')]"
        const result = await this.orm.call('crm.lead','calculate_start_and_end_dates',[ctx],{})
        if (this.isManager){
            if (ctx == 'all'){
                created_domain = "[('company_id', '=', "+company_id+"),('type', '=', 'opportunity')]"
                }
            else{
                created_domain = "[('company_id', '=', "+company_id+"),('type', '=', 'opportunity'),('create_date', '>=', '"+result.from_date+"'),('create_date', '<=', '"+result.to_date+"')]"
            }
        }
        else{
            if (ctx == 'all'){
                created_domain = "[('company_id', '=', "+company_id+"),('user_id', '=', "+user_id+"),('type', '=', 'opportunity')]"
            }
            else{
                created_domain = "[('company_id', '=', "+company_id+"),('type', '=', 'opportunity'),('create_date', '>=', '"+result.from_date+"'),('create_date', '<=', '"+result.to_date+"'),('user_id', '=', "+user_id+")]"
            }
        }
        this.action.doAction({
                name:'Opportunity',
                type: 'ir.actions.act_window',
                res_model: 'crm.lead',
                views: [[false, "list"]],
                view_mode: "list",
                domain: created_domain,
                target: "main",
            });
   }

}
CrmDashboard.template = "crm_dashboard.CrmDashboard";
actionRegistry.add("crm_dashboard_tag", CrmDashboard);

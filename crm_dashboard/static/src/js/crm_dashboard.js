/**@odoo-module **/
import { registry } from "@web/core/registry";
import { Component } from  "@odoo/owl";
import { useService } from "@web/core/utils/hooks";



const actionRegistry = registry.category("actions");
class CrmDashboard extends Component {
    setup() {
         this.orm = useService('orm')
         this._fetch_data()
   }
   _fetch_data(){
    this.orm.call('crm.lead','get_tiles_data',[],{}).then(function(result){
        console.log(document.getElementById("my_lead"))
        document.getElementById("my_lead").append(result.total_leads);
        document.getElementById("my_opportunity").append(result.total_opportunity);
        document.getElementById("revenue").append(result.currency + result.expected_revenue);
    })
   }

}
CrmDashboard.template = "crm_dashboard.CrmDashboard";
actionRegistry.add("crm_dashboard_tag", CrmDashboard);

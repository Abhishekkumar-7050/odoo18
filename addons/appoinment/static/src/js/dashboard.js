/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

import {loadJS} from "@web/core/assets"
const actionRegistry = registry.category("actions");
// const {onWillStart , useRef , onMounted } = owl
const {onWillStart , useRef , onMounted } = owl



class appoinmentDashboard extends Component {
      setup() {
        super.setup();
        // super.setup();

        this.orm = useService('orm');
        this.actionService = useService("action");
        this.startDateRef = useRef("startDateRef");
        this.endDateRef = useRef("endDateRef");


        this.chartRef = useRef('chart');
        this.pieChart = useRef("pieChart");


        onWillStart(async () => {
            await loadJS("https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js");
        });

       
  	

        onMounted(() => { 
            this._fetch_data();  
        });
        

   }




async _fetch_data(){
            // const startInput = document.getElementById("start_date");
            // const endInput = document.getElementById("end_date");

        
            const today = new Date();
            const oneYearAgo = new Date();
            oneYearAgo.setFullYear(today.getFullYear() - 1);
            // const formatDate = (d) => d.toISOString().split("T")[0];


            // const start_date = startInput?.value || ""
            // const end_date = endInput?.value || "";

            const start_date = this.startDateRef.el?.value || "";
            const end_date = this.endDateRef.el?.value || "";

            console.log("fun call");
            

            let result = await this.orm.call("appointment.dashboard", "fetch_data_for_dashboard",[], {
                    start_date: start_date,
                    end_date: end_date
                });
        if(result){    
        //     document.getElementById('new-header').innerHTML = `
            
        //     <span style="font-size: 14px; color:white ;padding-left :8px;">
        //         ${result.new_state_name}
        //     </span>
        // `;



            document.getElementById('pending-count').innerText =  result.pending_state_count
            document.getElementById('approved-count').innerText =  result.approved_state_count
            document.getElementById('rejected-count').innerText =  result.rejected_state_count
            document.getElementById('total-count').innerText =  result.done_state_count
            console.log(result.end_date)
            document.getElementById("till-now").innerText = `Till- now ${end_date || ""}`;


            // document.getElementById('approved-header').innerHTML = `
            //     <span style="font-size: 14px; height:20px; color: white; font-weight: bold; padding: 4px;">
            //      Count:   ${result.approved_state_count}
            //     </span>
            //     <span style="font-size: 14px; color: white; padding: 4px;">
            //         ${result.approved_state_name}
            //     </span>
            // `;

            // document.getElementById('rejected-header').innerHTML = `
            //     <span style="font-size: 14px; height:20px; color: white; font-weight: bold; padding: 4px;">
            //        Count :  ${result.rejected_state_count}
            //     </span>
            //     <span style="font-size: 14px; color: white; padding: 4px;">
            //         ${result.rejected_state_name}
            //     </span>
            // `;

            // document.getElementById('done-header').innerHTML = `
            //     <span style="font-size: 14px; height:20px; color: white; font-weight: bold; padding: 4px;">
            //        Count:  ${result.done_state_count}
            //     </span>
            //     <span style="font-size: 14px; color: white; padding: 4px;">
            //         ${result.done_state_name}
            //     </span>
            // `; 


               // Render the charts
       this.renderChart(result);
       this.renderPieChart(result);
        }
  }


async renderChart(result) {
    const labels = ["Pending", "Approved", "Rejected", "Total"];
    const counts = [
        result.pending_state_count || 0,
        result.approved_state_count || 0,
        result.rejected_state_count || 0,
        result.done_state_count || 0,
    ];

    // Destroy old chart if it exists
    if (this._barChartInstance) {
        this._barChartInstance.destroy();
    }

    const ctx = this.chartRef.el.getContext("2d");

    this._barChartInstance = new Chart(ctx, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                label: "Appointment status",
                data: counts,
                backgroundColor: [
                    "#DAA520", // Pending
                    "#28a745", // Approved
                    "#dc3545", // Rejected
                    "#6c757d", // Total
                ],
            }],
        },
        options: {
            responsive: false, 
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false,
                },
                tooltip: {
                    enabled: true,
                },
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        precision: 0,
                    },
                },
            },
        },
    });
}

  async renderPieChart(result) {
    const ctx = this.pieChart.el;
    if (!ctx) {
        console.warn("Pie chart canvas not found");
        return;
    }

    // Extract counts and labels dynamically from result
    const labels = [
        result.pending_state_name || 'Pending',
        result.approved_state_name || 'Approved',
        result.rejected_state_name || 'Rejected',
        result.done_state_name || 'Done'
    ];

    const data = [
        result.pending_state_count || 0,
        result.approved_state_count || 0,
        result.rejected_state_count || 0,
        result.done_state_count || 0
    ];

    const chartData = {
        labels: labels,
        datasets: [{
            label: 'Appointment Status',
            data: data,
            backgroundColor: ['#DAA520', '#28a745', '#dc3545', '#6c757d'],
            borderWidth: 1
        }]
    };

    const config = {
        type: 'pie',
        data: chartData,
        options: {
            responsive: false,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom'
                },
                title: {
                    display: true,
                    text: 'Appointment Distribution'
                }
            }
        }
    };

    if (this._pieChartInstance) {
        this._pieChartInstance.destroy();
    }

    this._pieChartInstance = new Chart(ctx, config);
}









onCreateNew() {
    this.actionService.doAction({
        type: 'ir.actions.act_window',
        name: 'Create Appointment',
        res_model: 'appointment.appointment',
        view_mode: 'form',
        target: 'current', 
        views: [[false, 'form']],
      
    });
}

onview_pending() {
    const startInput = document.getElementById("start_date");
    const endInput = document.getElementById("end_date");

    const start_date = startInput?.value || "";
    const end_date = endInput?.value || "";

    function addOneDay(dateStr) {
        const date = new Date(dateStr);
        date.setDate(date.getDate() + 1);
        return date.toISOString().split("T")[0];
    }

    console.log("Start:", start_date, "End:", end_date); 

    const domain = [['state', '=', 'pending']];

    if (start_date) {
        domain.push(['appoinnment_date', '>=', start_date]);
    }

    if (end_date) {
        const end_date_next = addOneDay(end_date);  // to include full day
        domain.push(['appoinnment_date', '<', end_date_next]);
    }

    this.actionService.doAction({
        type: 'ir.actions.act_window',
        name: 'Pending Appointments',
        res_model: 'appointment.appointment',
        view_mode: 'list,form',
        views: [[false, 'list'], [false, 'form']],
        domain: domain,
        target: 'current',
    });
}

onview_approved() {
    const startInput = document.getElementById("start_date");
    const endInput = document.getElementById("end_date");

    const start_date = startInput?.value || "";
    const end_date = endInput?.value || "";

    function addOneDay(dateStr) {
        const date = new Date(dateStr);
        date.setDate(date.getDate() + 1);
        return date.toISOString().split("T")[0];
    }

    console.log("Start:", start_date, "End:", end_date); 

    const domain = [['state', '=', 'approved']];

    if (start_date) {
        domain.push(['appoinnment_date', '>=', start_date]);
    }

    if (end_date) {
        const end_date_next = addOneDay(end_date);  // to include full day
        domain.push(['appoinnment_date', '<', end_date_next]);
    }
        
     this.actionService.doAction({
        type: 'ir.actions.act_window',
        name: 'Pending Appointments',
        res_model: 'appointment.appointment',
        view_mode: 'list,form', 
        views: [[false, 'list'], [false, 'form']],
        domain: domain,
        target: 'current',  
     
    });
}
onview_reject() {
    const startInput = document.getElementById("start_date");
    const endInput = document.getElementById("end_date");

    const start_date = startInput?.value || "";
    const end_date = endInput?.value || "";

    function addOneDay(dateStr) {
        const date = new Date(dateStr);
        date.setDate(date.getDate() + 1);
        return date.toISOString().split("T")[0];
    }

    console.log("Start:", start_date, "End:", end_date); 

    const domain = [['state', '=', 'rejected']];

    if (start_date) {
        domain.push(['appoinnment_date', '>=', start_date]);
    }

    if (end_date) {
        const end_date_next = addOneDay(end_date);  // to include full day
        domain.push(['appoinnment_date', '<', end_date_next]);
    }
       
     this.actionService.doAction({
        type: 'ir.actions.act_window',
        name: 'Pending Appointments',
        res_model: 'appointment.appointment',
        view_mode: 'list,form', 
        views: [[false, 'list'], [false, 'form']],
        domain: domain,
        target: 'current',  
     
    });

}

onview_total() {
    const startInput = document.getElementById("start_date");
    const endInput = document.getElementById("end_date");

    const start_date = startInput?.value || "";
    const end_date = endInput?.value || "";

    function addOneDay(dateStr) {
        const date = new Date(dateStr);
        date.setDate(date.getDate() + 1);
        return date.toISOString().split("T")[0];
    }

    console.log("Start:", start_date, "End:", end_date); 

    const domain = [];

    if (start_date) {
        domain.push(['appoinnment_date', '>=', start_date]);
    }

    if (end_date) {
        const end_date_next = addOneDay(end_date);  // to include full day
        domain.push(['appoinnment_date', '<', end_date_next]);
    }
       
     this.actionService.doAction({
        type: 'ir.actions.act_window',
        name: 'Pending Appointments',
        res_model: 'appointment.appointment',
        view_mode: 'list,form', 
        views: [[false, 'list'], [false, 'form']],
        domain: domain,
        target: 'current',  
     
    });

}



}
appoinmentDashboard.template = "appoinment.appDashboard";
// Register the component with the action tag
actionRegistry.add("appoinment_dashboard_tag", appoinmentDashboard);






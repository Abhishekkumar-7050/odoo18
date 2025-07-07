
/** @odoo-module */

import { registry } from "@web/core/registry";
import { Layout } from "@web/search/layout";
import { getDefaultConfig } from "@web/views/view";
import { useService } from "@web/core/utils/hooks";
import {useState } from "@odoo/owl";
const { Component, useSubEnv } = owl;

export class OwlOdooServices extends Component {
    // static template = 'OdooServices'
    
    setup() {
        this.state = useState({
            patients :[]
        })
        
        console.log("Owl Odoo Services");
        this.orm = useService("orm");
        this.display = {
            controlPanel: {"top-right": false, "bottom-right": false }
        };
        useSubEnv({
            config: {
                ...getDefaultConfig(),
                ...this.env.config,
            },
        })
        console.log("nsdhjfbdbj");
        
    }

    async getPatient() {
    try {
        const result = await this.orm.call(
            'patient.patient', 
            'search_read', 
            [], 
            { }
        );
        this.state.patients = result
        console.log(result);
    } catch (error) {
        console.error(error);
    }
}
}

OwlOdooServices.template = "owl.OdooServices";
OwlOdooServices.components ={Layout};

registry.category("actions").add("owl.OdooServices", OwlOdooServices);
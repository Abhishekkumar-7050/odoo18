from odoo import models, fields, api

class AppointmentDashboard(models.TransientModel):
    _name = 'appointment.dashboard'
    _description = 'Appointment Dashboard'

    new_state_count = fields.Integer(string="New", compute="_compute_state_count")
    new_state_name = fields.Char(string="Name", compute="_compute_state_count")

    pending_state_count = fields.Integer(string="Pending", compute="_compute_state_count")
    pending_state_name = fields.Char(string="Name", compute="_compute_state_count")

    approved_state_count = fields.Integer(string="Approved", compute="_compute_state_count")
    approved_state_name = fields.Char(string="Name", compute="_compute_state_count")

    rejected_state_count = fields.Integer(string="Rejected", compute="_compute_state_count")
    rejected_state_name = fields.Char(string="Name", compute="_compute_state_count")

    done_state_count = fields.Integer(string="Done", compute="_compute_state_count")
    done_state_name = fields.Char(string="Name", compute="_compute_state_count")

    
    def _compute_state_count(self):
        # import pdb; pdb.set_trace()
        Appointment = self.env['appointment.appointment']
        for rec in self:
            rec.new_state_count = Appointment.search_count([('state', '=', 'new')])
            rec.new_state_name = "New Appointments"

            rec.pending_state_count = Appointment.search_count([('state', '=', 'pending')])
            rec.pending_state_name = "Pending Appointments"

            rec.approved_state_count = Appointment.search_count([('state', '=', 'approved')])
            rec.approved_state_name = "Approved Appointments"

            rec.rejected_state_count = Appointment.search_count([('state', '=', 'rejected')])
            rec.rejected_state_name = "Rejected Appointments"

            rec.done_state_count = Appointment.search_count([])
            rec.done_state_name = "Total"

    
 


 

    @api.model
    def open_dashboard(self):
          # Delete old transient records (optional cleanup)
        self.search([]).unlink()
    # Create one temporary record to trigger computation
        record = self.create({})
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'appointment.dashboard',
            'view_mode': 'kanban',
            'res_id': record.id,
            'target': 'current',
        }

    


    def action_open_new_appointments(self):
        return self.action_open_filtered_appointments('new')

    def action_open_pending_appointments(self):
        return self.action_open_filtered_appointments('pending')

    def action_open_approved_appointments(self):
        return self.action_open_filtered_appointments('approved')

    def action_open_rejected_appointments(self):
        return self.action_open_filtered_appointments('rejected')

    def action_open_done_appointments(self):
        return self.action_open_filtered_appointments('done')
    



    def action_open_filtered_appointments(self, state):
      
        return {
            'type': 'ir.actions.act_window',
            'name': 'Filtered Appointments',
            'res_model': 'appointment.appointment',
            'view_mode': 'list,form',
            'domain': [('state', '=', state)],
            'target': 'current',
        }


    



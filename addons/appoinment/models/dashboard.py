from odoo import models, fields, api
from datetime import datetime, time
from datetime import time


class AppointmentDashboard(models.TransientModel):
    _name = 'appointment.dashboard'
    _description = 'Appointment Dashboard'

    # new_state_count = fields.Integer(string="New", compute="_compute_state_count")
    # new_state_name = fields.Char(string="Name", compute="_compute_state_count")

    # pending_state_count = fields.Integer(string="Pending", compute="_compute_state_count")
    # pending_state_name = fields.Char(string="Name", compute="_compute_state_count")

    # approved_state_count = fields.Integer(string="Approved", compute="_compute_state_count")
    # approved_state_name = fields.Char(string="Name", compute="_compute_state_count")

    # rejected_state_count = fields.Integer(string="Rejected", compute="_compute_state_count")
    # rejected_state_name = fields.Char(string="Name", compute="_compute_state_count")

    # done_state_count = fields.Integer(string="Done", compute="_compute_state_count")
    # done_state_name = fields.Char(string="Name", compute="_compute_state_count")

    
    # def _compute_state_count(self):
    #     # import pdb; pdb.set_trace()
    #     Appointment = self.env['appointment.appointment']
    #     for rec in self:
    #         rec.new_state_count = Appointment.search_count([('state', '=', 'new')])
    #         rec.new_state_name = "New Appointments"

    #         rec.pending_state_count = Appointment.search_count([('state', '=', 'pending')])
    #         rec.pending_state_name = "Pending Appointments"

    #         rec.approved_state_count = Appointment.search_count([('state', '=', 'approved')])
    #         rec.approved_state_name = "Approved Appointments"

    #         rec.rejected_state_count = Appointment.search_count([('state', '=', 'rejected')])
    #         rec.rejected_state_name = "Rejected Appointments"

    #         rec.done_state_count = Appointment.search_count([])
    #         rec.done_state_name = "Total"

    
 


 

    # @api.model
    # def open_dashboard(self):
    #       # Delete old transient records (optional cleanup)
    #     self.search([]).unlink()
    # # Create one temporary record to trigger computation
    #     record = self.create({})
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'appointment.dashboard',
    #         'view_mode': 'kanban',
    #         'res_id': record.id,
    #         'target': 'current',
    #     }

    


    # def action_open_new_appointments(self):
    #     return self.action_open_filtered_appointments('new')

    # def action_open_pending_appointments(self):
    #     return self.action_open_filtered_appointments('pending')

    # def action_open_approved_appointments(self):
    #     return self.action_open_filtered_appointments('approved')

    # def action_open_rejected_appointments(self):
    #     return self.action_open_filtered_appointments('rejected')

    # def action_open_done_appointments(self):
    #     return self.action_open_filtered_appointments('done')
    



    # def action_open_filtered_appointments(self, state):
      
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Filtered Appointments',
    #         'res_model': 'appointment.appointment',
    #         'view_mode': 'list,form',
    #         'domain': [('state', '=', state)],
    #         'target': 'current',
    #     }


    

    @api.model
    def fetch_data_for_dashboard(self, **kwargs):
        start_date = kwargs.get('start_date')
        end_date = kwargs.get('end_date')

        # Appointment = self.env['appointment.appointment']
        # new_state_count = Appointment.search_count([('state', '=', 'new')])
        # new_state_name = "New Appointments"

        # pending_state_count = Appointment.search_count([('state', '=', 'pending')])
        # pending_state_name = "Pending Appointments"

        # approved_state_count = Appointment.search_count([('state', '=', 'approved')])
        # approved_state_name = "Approved Appointments"

        # rejected_state_count = Appointment.search_count([('state', '=', 'rejected')])
        # rejected_state_name = "Rejected Appointments"

        # done_state_count = Appointment.search_count([])
        # done_state_name = "Total"

        # return{
        #     'new_state_count': new_state_count,
        #     'new_state_name':new_state_name,
        #     'pending_state_count': pending_state_count,
        #     'pending_state_name': pending_state_name,
        #     'approved_state_count': approved_state_count,
        #     'approved_state_name':approved_state_name,
        #     'rejected_state_count': rejected_state_count,
        #     'rejected_state_name': rejected_state_name,
        #     'done_state_count': done_state_count,
        #     'done_state_name': done_state_name
            


        # }
        start_date = kwargs.get('start_date')
        end_date = kwargs.get('end_date')

        domain = []

     



        # If start_date is provided → apply >= filter
        if start_date:
            start_date_obj = fields.Date.from_string(start_date)
            start_dt = datetime.combine(start_date_obj, time.min)
            start_dt_str = fields.Datetime.to_string(start_dt)
            domain.append(('appoinnment_date', '>=', start_dt_str))

        # If end_date is provided → apply <= filter
        if end_date:
            end_date_obj = fields.Date.from_string(end_date)
            end_dt = datetime.combine(end_date_obj, time.max)
            end_dt_str = fields.Datetime.to_string(end_dt)
            domain.append(('appoinnment_date', '<=', end_dt_str))

            # Search between full datetime range
        # domain = [('appoinnment_date', '>=', start_dt_str), ('appoinnment_date', '<=', end_dt_str)]

        appointments = self.env['appointment.appointment'].search(domain)

        # Count by state
        return {
            'new_state_count': len(appointments.filtered(lambda r: r.state == 'new')),
            'new_state_name': 'New',
            'pending_state_count': len(appointments.filtered(lambda r: r.state == 'pending')),
            'pending_state_name': 'Pending',
            'approved_state_count': len(appointments.filtered(lambda r: r.state == 'approved')),
            'approved_state_name': 'Approved',
            'rejected_state_count': len(appointments.filtered(lambda r: r.state == 'rejected')),
            'rejected_state_name': 'Rejected',
            'done_state_count': len(self.env['appointment.appointment'].search(domain)),
            'done_state_name': 'Total',
            'end_date': end_date or ""
        }
        

from odoo import models , fields  ,api


class AppointmentGroup(models.Model):
    _name = "appointment.group"


    group_name =  fields.Char(string = "Group Name" , required=True)
    appointees_ids = fields.Many2many( string = "Apoointess",  comodel_name="appointment.appointees" , inverse_name='group_id', copy=True, auto_join=True)

    appointment_charge = fields.Integer(string = " Appointment Charge", required = True)
    group_product = fields.Char(string = "Product", required = True)
    group_image = fields.Binary(string = "Image" ) 

    discription = fields.Char(string = "Description" )

    appointment_ids = fields.Many2many('appoitment.appointment')

    sub_total = fields.Float(string="Sub Total", compute="_compute_sub_total", store=True)
    appointment_count = fields.Integer(string="Total Appointments", compute="_compute_appointment_count", store=True)

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = len(rec.appointment_ids)


    appointment_id = fields.Many2one('appointment.appointment' , index=True, copy=False)

    

    @api.depends('appointment_charge')
    def _compute_sub_total(self):
        for rec in self:
            rec.sub_total = rec.appointment_charge

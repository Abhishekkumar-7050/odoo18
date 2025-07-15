from odoo import models , fields , api


class Appointees(models.Model):
    _name="appointment.appointees"

    name =  fields.Char(string = "Name")

    allow_multiple = fields.Boolean(string = "Allow the multiple appointments")

    street = fields.Char()
    city = fields.Char()
    country_id = fields.Many2one('res.country')
    state_id = fields.Many2one('res.country.state')
    zip = fields.Integer(string = "Zip")

    image = fields.Binary(string ="Image")

  
    company_id = fields.Many2one('res.company', string="Company")

    
    phone = fields.Char("Phone Nu:")
    email = fields.Char("Email:")
    appointments_charges = fields.Integer(string = "appointments Charge")

    experience = fields.Integer(string="Experience (Years):")
    specialist_in = fields.Char(string="Specialist In")
    about = fields.Text(string="About")
    note = fields.Text(string="Important Notes")
    

    time_slot_line = fields.Many2many(
        comodel_name='appointment.time_slot',
        inverse_name='appointees_id',
        string="Time Slot",
        copy=True, auto_join=True)
    

    appointment_ids = fields.One2many(
        comodel_name='appointment.appointment', 
        inverse_name='appointees_id',           
        string='All Appointments',              
        readonly=True                            
    )


    group_id = fields.Many2many('appointment.group')


    








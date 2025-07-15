from odoo import models , fields , api


class Appointees(models.Model):
    _name="appointment.appointees"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name =  fields.Char(string = "Name" ,required= True)

    allow_multiple = fields.Boolean(string = "Allow the multiple appointments")

    street = fields.Char(required= True)
    city = fields.Char(required= True)
    country_id = fields.Many2one('res.country',required= True)
    state_id = fields.Many2one('res.country.state',required= True)
    zip = fields.Integer(string = "Zip")

    image = fields.Image(string ="Image")

  
    company_id = fields.Many2one('res.company', string="Company")

    
    phone = fields.Char("Phone Nu:",required= True)
    email = fields.Char("Email:",required= True)
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


    def action_open_groups(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Groups',
            'view_mode': 'list,form',
            'res_model': 'appointment.group',
            'domain': [('id', 'in', self.group_id.ids)],
            'context': {'default_appointees_ids': [self.id]},
        }



    








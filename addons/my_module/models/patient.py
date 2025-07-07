from odoo import models, fields , api
from datetime import datetime , timedelta ,date
import base64
from odoo.exceptions import ValidationError



class Patient(models.Model):
    _name = "patient.patient"


    name = fields.Char(string = "Name" , requred=True)

    dob = fields.Datetime(default=lambda self: datetime.now() , requred=True)
    # age = fields.Integer( readOnly =True) 

    number = fields.Char(string ="Phone Nu :",requred=True )

    email = fields.Char(string = " Email" , requred=True)

    age = fields.Integer( readOnly =True ,  compute='_compute_age') 

    gender = fields.Selection([("male","male"), ("female","female")])

    company= fields.Many2one('res.company')

    
    image = fields.Binary(string="Upload Photo")

    
    # to_store_basestring = fields.Binary(string="Base64 String", compute='_compute_into_basestring',)
    # image_bytes = fields.Binary(string="Decoded Image", compute='_decode_base64', String ="image")

    # @api.depends('image')
    # def _compute_into_basestring(self):
    #         for record in self:
    #             if record.image:
    #                 data = record.image.read()
    #                 record.to_store_basestring = base64.b64encode(data)



    @api.depends('dob')
    def _compute_age(self):
        for rec in self:
            if rec.dob:
                today = date.today()
                dob_date = rec.dob.date()  
                rec.age = today.year - dob_date.year 
            else:
                rec.age = 0


    @api.constrains('dob')
    def _check_dob_not_in_future(self):
        for rec in self:
            if rec.dob and rec.dob > datetime.now():
                raise ValidationError("Date of Birth must be To day or before doday.")
            


    _sql_constraints = [
            ('name_not_be_empty',
            'UNIQUE(email)',
            'Email alredy exists .',),
            ]


    






   

from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError

class School(models.Model):
    _name = 'school.school'
    _description = 'school'
    _rec_name = 'school_name'
    school_id =  fields.Integer()
    school_name = fields.Char(string='School Name')
    address = fields.Char(String= 'Address of  school')
    Email = fields.Char(string ="Email")
    students = fields.One2many('student.student', 'school_id')






    _sql_constraints = [
         ('unique_school_name',
         'UNIQUE(school_name)',
         'school_name name  already exists!'),
    ]
  

    # @api.constrains('school_name')
    # def check_school_name(self):
    #     # import pdb; pdb.set_trace()

    #     records = self.env['school.school'].search([])

    #     for record in records :

    #         if record.school_name == self.school_name:
    #          raise ValidationError('School name')



        # if self.school_name == False:

        #      raise ValidationError('School name')

        

    

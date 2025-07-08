from odoo import models, fields,api
from datetime import datetime, timedelta
import logging

_logger = logging.getLogger("My Custom Logger")


class Customer(models.Model):
    _name = 'customer.customer'
    _description = 'customer'
    _rec_name = 'first_name'
    


    
    first_name =  fields.Char(string= 'First Name')
    last_name =  fields.Char(string= 'Last Name')
    age = fields.Integer()
    country = fields.Char(string = 'Country Name')

    order_id =  fields.One2many('order.order', 'customer_id')

    total_amount =  fields.Integer(string = 'Total amount',compute ='compute_amount' )




    _sql_constraints = [
        ('unique_customer_name',
         'UNIQUE(first_name)',
         'first name  already exists!'),
         

        ('customer_age_positive',
         'CHECK(age >= 0)',
         'Customer age cannot be negative.'),

        ('customer_name_not_empty',
         "CHECK(first_name IS NOT NULL AND first_name != '')",
         'First name cannot be empty.'),

          ('custome_last_name_not_empty',
         "CHECK(last_name IS NOT NULL AND last_name != '')",
         'last name cannot be empty.'),


        ('customer_country_uppercase',
         "CHECK(country = UPPER(country) OR country IS NULL OR country = '')",
         'Country name should be in uppercase or empty.'),

        ('total_amount_non_negative',
         'CHECK(total_amount >= 0)',
         'Total amount cannot be negative.'),
    ]


    
    
    def open_wizard(self):
        return {
            'name': 'Customer Name',
            'type': 'ir.actions.act_window',
            'view_mode' : 'form',
            'res_model' : 'customer_wizard',
            'target':'new',
            'context': {'customer_rec_id' : self.id}
        }




    
    @api.depends('order_id')
    def compute_amount(self):

        # orders =  self.env['order.order'].search([])
        for rec in self:
            rec.total_amount = 0

            for order in rec.order_id :
                rec.total_amount += int(order.amount)
                _logger.info(f'======rec{rec.total_amount}============')



    #  display name  orm
    @api.depends('first_name', 'last_name')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.first_name} -> {record.last_name}" if record.first_name else record.last_name



    
    @api.model
    def my_model_method(self):
        # code that does not rely on a particular record
        __loader__.info( "This method can be called without records")
        
    
    
    @api.model_create_multi
    def create(self, vals_list):
        # Optimized creation of multiple records
        return super(Customer, self).create(vals_list)





        

    
            
            


        

        














    
  

    

    

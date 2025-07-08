from odoo import models, fields,api
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta

class Order(models.Model):
    _name = 'order.order'
    _description = 'order'
    


    
    item =  fields.Char(string= 'Name of Item')
    amount =  fields.Integer(string= 'Price of Item')
    discount = fields.Boolean(default=0)
    customer_id =  fields.Many2one('customer.customer')


    _sql_constraints = [
        
        ('check_amount_positive', 'check(amount >= 0)', 'The price of the item must be positive!'),
        ('check_more_than_100' , 'check(dicount > 100 )', 'Discount  cannot be more than 100%')
    ]



    
    def open_wizard(self):
        return {
            'name': 'Select Customer',
            'type': 'ir.actions.act_window',
            'view_mode' : 'form',
            'res_model' : 'order.wizard',
            'target':'new',
            'context': {'customer_rec_id' : self.id}
        }

    

    @api.model
    def default_get(self, item):
        fields = self.env['order.order'].fields_get()
        res = super(Order, self).default_get(fields)
        # Custom logic to add or modify default values
        if 'item' in fields:
            res['item'] = 'Laptop'
        return res
        
   

    # discount_amount = 5
    # @api.depends_context('discount_amount')
    @api.onchange('discount')
    def onchange_discount(self):
        discount_amount = self.env.context.get('discount_amount', 5.0)

        if self.discount:
            self.amount -= discount_amount





    
      # contraint decorator
    @api.constrains('amount')
    def _check_price_quantity(self):
        for record in self:
            if record.amount < 0 :
                raise ValidationError("Price and quantity must be positive.")
            

    

    # ti create the multi records takes a list in as argument
    @api.model_create_multi
    def create(self, vals_list):

        # Optimized creation of multiple records
        return super(Order, self).create(vals_list)


  












    
  

    

    

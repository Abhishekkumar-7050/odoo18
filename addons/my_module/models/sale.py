from odoo import models, fields ,api 
from odoo.exceptions import ValidationError

import logging

_logger = logging.getLogger("My Custom Logger")



class Sale(models.Model):
    _inherit= 'sale.order'

    new_field = fields.Char(String="New Field added")
    second_field = fields.Char(String ="Second field added")

    
    def _compute_amounts(self):
       
    # #    _logger.info(f'{self.partner_id.vip_customer} " ======================"')

    # #    if self.partner_id.vip_customer == True:
    # #       pass

        super()._compute_amounts()

        if self.partner_id.vip_customer == True:
           self.amount_total -=   (5/100) * self.amount_total
    #     # _logger.info(f'{self.partner_id.vip_customer} " ======={self.amount_total}==============="')    
    

    def _compute_tax_totals(self):


        temp = super()._compute_tax_totals()
        # import pdb; pdb.set_trace()

        self.tax_totals['total_amount_currency'] = self.amount_total
        return temp



             

          


class ResPartner(models.Model):
    _inherit= 'res.partner'

    vip_customer = fields.Boolean(string ="VIP Customer")



    

class Orderline(models.Model):
    _inherit= 'sale.order.line'


    discount = fields.Float(
        
        string="Discount",
        compute='_computediscount',
        # store=True, readonly=False, 
        # context={'active_test': False},
        # check_company=True
        default= 10,
    )
    _sql_constraints = [
        ('dicount_check',
         'CHECK(discount < 100)',
         'DISCOUNT CANNOT 100% AND MORE THAN 100%')
    ]

    @api.constrains('discount')
    def _check_discount(self):
        for record in self:
            if record.discount < 0  or record.discount > 100 :
                raise ValidationError(" Invalid Discount  discount should be 1 to 100 %!.")
            
        _logger.error(f'discount validation failed')

  

    @api.depends('product_uom_qty','product_id.categ_id')
    def _compute_discount(self):
     for record in self:
        record.discount = 0

        
        if record.product_uom_qty >= 10:
            record.discount += 10
    
        if record.product_id.categ_id.name == 'electronics':
            record.discount += 5
        








    
   
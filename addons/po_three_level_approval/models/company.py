from odoo import models, fields ,api 
from odoo.exceptions import ValidationError





class Comapany(models.Model):
    _inherit= 'res.company'

    level_approval = fields.Boolean(string = "Three Level Approval")
    manager_approval = fields.Integer(string="Manager approve limit")
    finance_approval = fields.Integer(string= "Finance approve limit")
    director_approval = fields.Integer(string= "Director approve limit")
    email_approval = fields.Many2one(
        'mail.template',
        string="Approval Email Template",
        readonly='1',
        # default=lambda self: self.env['ir.model.data']._xmlid_to_res_id('po_three_level_approval.email_template_edi_purchase_approval')
    )
    
    refuse_email_approval = fields.Many2one(
        'mail.template',
        string="Refuse Email Template",
        readonly='1',
        # default=lambda self: self.env['ir.model.data']._xmlid_to_res_id('po_three_level_approval.email_template_edi_refuse_approval')
    
    )


    # contraint decorator
    @api.constrains('manager_approval' , 'finance_approval' ,'director_approval')
    def check(self):
       
        if self.finance_approval < self.manager_approval :
            raise ValidationError("Finance Limit must be greater then manager limit")
        elif self.director_approval < self.manager_approval :
            raise ValidationError("Director Limit must be greater then manager limit")
        elif self.director_approval < self.finance_approval:
             raise ValidationError("Director Limit must be greater then Finance Limit")
        elif self.manager_approval < 0 :
            raise ValidationError("limit not be negative ")
        elif self.finance_approval < 0 :
            raise ValidationError("limit not be negative ")
        elif self.director_approval < 0 :
            raise ValidationError("limit not be negative ")




            
            









    



  
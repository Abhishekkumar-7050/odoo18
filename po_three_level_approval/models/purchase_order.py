from odoo import models, fields ,api 
from odoo.exceptions import ValidationError


class Purchase(models.Model):
    _inherit= 'purchase.order'


    state = fields.Selection([
    ('draft', 'RFQ'),
    ('sent', 'RFQ Sent'),
    ('to approve', 'To Approve'),
    ('done', 'Locked'),
    ('cancel', 'Cancelled'),
    ('manager', 'Manager Approve'),
    ('managerwait', 'Waiting for Manager Approval'),
    ('financewait', 'Waiting for Finance Approval'),
    ('finace', 'Finance Approve'),
    ('directorwait', 'Waiting for Director Approval'),
    ('director', 'Director Approve'),
    ('refuse', 'Refused'),
    ('purchase', 'Purchase Order'),
    ], string='Status', readonly=True, index=True, copy=False, default='draft', tracking=True)



    managerApprovals = fields.Char( string="Manager Approval", store=True)
    financeApprovals = fields.Char( string="Finance Approval", store=True)
    directorApprovals = fields.Char( string="Director Approval", store=True)

    purchaseManagers = fields.Char(
       
        string="Purchase Manager",
        store=True
    )
    purchaseFinances = fields.Char(
        
        string="Finance Manager",
        store=True
    )
    purchaseDirectors = fields.Char(
     
        string="Director Manager",
        store=True
    )
    manager_approval_date = fields.Datetime(string="Manager Approval Date")
    finance_approval_date = fields.Datetime(string="Finance Approval Date")
    director_approval_date = fields.Datetime(string="Director Approval Date")

    refuse_resson = fields.Char(string="Refuse Reason")
    refused_By = fields.Char(string="Refused by")
    refused_date = fields.Date(string = "Refused Date")


    
 

    def button_approve(self, force=False):
        amount = self.amount_total
        company = self.company_id
        finance_limit = company.finance_approval 
        director_limit = company.director_approval 


        if self.env.user.has_group('po_three_level_approval.group_of_manager_company'):
            self.purchaseManagers =  self.env.user.name
            self.managerApprovals = self.env.user.name
            self.manager_approval_date = self.date_order

        if self.env.user.has_group('po_three_level_approval.group_of_Finace'):
          self.financeApprovals = self.env.user.name
          self.purchaseFinances = self.env.user.name
          self.finace_approval_date = self.date_order

        if self.env.user.has_group('po_three_level_approval.group_of_director'):
          self.directorApprovals = self.env.user.name
          self.purchaseFinances = self.env.user.name
          self.director_approval_date = self.date_order
      
        

#manager handling
        if self.state == "managerwait" and amount > finance_limit:
             print("mannagerwait")
             if finance_limit == 0 and director_limit != 0 :
                  self.write({'state': 'directorwait'}) 
             elif finance_limit == 0 and director_limit ==0 :   
                 self.write({'state': 'purchase'})
             else:
                 self.write({'state': 'financewait'})
        elif self.state == "manager" and amount > finance_limit :
              print("manager")
              if finance_limit == 0 and director_limit != 0 :
                  self.write({'state': 'directorwait'})  
              elif finance_limit == 0 and director_limit ==0 :   
                 self.write({'state': 'purchase'})
              else:
             
                self.write({'state': 'financewait'})


# finance handling
        elif self.state == "financewait" and amount > director_limit :
            print("finance wait")
            if director_limit == 0:
                self.write({'state': 'purchase'})
            else:
                self.write({'state': 'directorwait'})
        elif self.state == "finace" and amount > director_limit :
            print("finance")
            if director_limit == 0:
                self.write({'state': 'purchase'})
            else:
                self.write({'state': 'directorwait'})

# director handling
        elif self.state == "directorwait" and amount > director_limit:
            print("director wait")
            self.write({'state': 'purchase'})
        else:
             self.write({'state': 'purchase'})


        
        self.action_send_mail_()
     
      


    def button_confirm(self):
        self.ensure_one()

        approval_levels = self._approval_allowed()
        # import pdb; pdb.set_trace()
       

        amount = self.amount_total
        company = self.company_id
        Is_approval = self.company_id.level_approval

        finance_limit = company.finance_approval 
        manager_limit = company.manager_approval 
        director_limit = company.director_approval 

       
        if 'user' in  approval_levels and amount > manager_limit  and self.env.user.has_group('po_three_level_approval.group_of_user') :
            if manager_limit == 0  and finance_limit != 0 :
                 self.write({'state':'financewait'})
            elif manager_limit == 0 and finance_limit == 0 and director_limit != 0:
                 self.write({'state':'directorwait'})
            elif manager_limit == 0 and finance_limit == 0 and director_limit == 0:
                 self.write({'state': 'purchase'})
                 print("user exists")
            else:
                self.write({'state':'managerwait'})

        elif 'director' in approval_levels and director_limit!= 0 and self.env.user.has_group('po_three_level_approval.group_of_director'):
                self.write({'state': 'director'})
        elif 'manager' in approval_levels and manager_limit != 0 and self.env.user.has_group('po_three_level_approval.group_of_manager_company'):
                print("kru nhi gya")
                self.write({'state': 'manager'})
        elif 'finace' in approval_levels and finance_limit != 0 and self.env.user.has_group('po_three_level_approval.group_of_Finace'):
                self.write({'state': 'finace'})
        else:
                    self.write({'state': 'purchase'})

        if self.state !=  'purchase':
           self.action_send_mail_()
       




    def _approval_allowed(self):

        self.ensure_one()
        approval_dict = {}

        # import pdb; pdb.set_trace()
        amount = self.amount_total
        company = self.company_id
        Is_approval = self.company_id.level_approval

        finance_limit = company.finance_approval 
        manager_limit = company.manager_approval 
        director_limit = company.director_approval 

        if manager_limit == 0:
            self.write({'state':'managerwait'})
        
    

    
        if  amount >= finance_limit and Is_approval and finance_limit != 0:
          approval_dict['finace'] = True

        if amount >= manager_limit and Is_approval and manager_limit != 0:
          approval_dict['manager'] = True

        if amount >= director_limit and Is_approval and director_limit !=0 :
         approval_dict['director'] = True
        
        if amount > 0 and self.env.user.has_group('po_three_level_approval.group_of_user')  and Is_approval :
           approval_dict['user'] = True

        print(approval_dict)
    
        return approval_dict
    

    def action_send_mail_for_refuse(self):
        template = self.env.ref('po_three_level_approval.email_template_edi_refuse_approval')
        email_values = {'email_from': self.env.user.email}
        template.send_mail(self.id, force_send=True, email_values=email_values)


  
    


    # def refuse_btn(self):
    #     self.write({'state':'refuse'})
    #     self.action_send_mail_for_refuse()
       


    def action_send_mail_(self):
        template = self.env.ref('po_three_level_approval.email_template_edi_purchase_approval')
        email_values = {'email_from': self.env.user.email}
        name= "user"
        if self.state == "managerwait":
            name= "Manager"
        elif self.state == "financewait":
            name = "Finance Manager"
        elif self.state == "directorwait":
             name = "Director Manager"
        ctx = {
            'object': self,
            'name' : name

        }
        template.with_context(ctx).send_mail(self.id, force_send=True, email_values=email_values)
    


    def action_send_mail_for_refuse(self):
        template = self.env.ref('po_three_level_approval.email_template_edi_refuse_approval')
        email_values = {'email_from': self.env.user.email}
        ctx = {
        'object': self,
        'mail_to': 'purchasemanager@gmail.com',
        'name' : "Purchase Manager"
    }
        
        template.with_context(ctx).send_mail(self.id, force_send=True, email_values=email_values)
    


     
    def action_refuse(self):
        # self.write({'state':'refuse'})
        # self.action_send_mail_for_refuse()
        return {
            'name': 'Customer Name',
            'type': 'ir.actions.act_window',
            'view_mode' : 'form',
            'res_model' : 'refuse.refuse',
            'target':'new',
            
        }
        
            


        




















   
        

    



        














  
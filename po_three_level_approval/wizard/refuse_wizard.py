from odoo import models, fields, api
from datetime import datetime , timedelta ,date





class Refuse(models.TransientModel):
    _name = 'refuse.refuse'

    reason =  fields.Char(string= 'Reason Of refuse' , required=True)



    def button_confirm_refuse(self):
        active_id = self.env.context.get('active_id')
        if active_id:
            order = self.env['purchase.order'].browse(active_id)
            order.refuse_resson = self.reason
            order.refused_By = self.env.user.name
            order.refused_date =  datetime.now()

            order.write({'state':'refuse'})
            order.action_send_mail_for_refuse()
    

    



    

        # record.first_name.id = self.id

        # record.first_name = self.first_name


     
     

    







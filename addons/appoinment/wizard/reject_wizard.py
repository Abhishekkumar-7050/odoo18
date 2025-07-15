from odoo import models, fields, api
from datetime import datetime , timedelta ,date



class AppointmentReject(models.TransientModel):
    _name = 'appointment.reject'
    reason =  fields.Char(string= 'Reason Of reject' , required=True)



    def button_confirm_reject(self):
        active_id = self.env.context.get('active_id')
        if active_id:
            appointment = self.env['appointment.appointment'].browse(active_id)
            appointment.reject_resson = self.reason
            # appointment.write({'state':'rejected'})
            appointment.action_reject()
    

    



    


     
     

    







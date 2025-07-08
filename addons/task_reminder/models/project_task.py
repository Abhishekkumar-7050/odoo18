from odoo import models, fields ,api 
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta ,time
from datetime import date 





class Sale(models.Model):
    _inherit= 'project.task'



    def action_send_mail_task_reminder(self):

        today = datetime.today().date()
        start_of_day = datetime.combine(today, time.min)  
        end_of_day = datetime.combine(today, time.max)    


        tasks = self.env['project.task'].search([
            ('date_deadline', '>=', start_of_day),
            ('date_deadline', '<=', end_of_day)
        ])

        
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        # print('----------',base_url)

        for task in tasks:
            template = self.env.ref('task_reminder.mail_to_user_deadline_template_id', raise_if_not_found=False)
            if template:
                task_url = f"{base_url}/odoo/all-tasks/{task.id}"
                email_ctx ={
                    'task_url':task_url,
                    'name' : self.env.user.name,
                }
                email_values = {'email_from': self.env.user.email}
                template.with_context(email_ctx).send_mail(task.id, force_send=True, email_values=email_values)
                task.message_post(body="Deadline reminder email sent.")
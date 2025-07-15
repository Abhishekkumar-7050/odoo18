from odoo import models, fields ,api 
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta ,time
from datetime import date 





class Task(models.Model):
    _inherit= 'project.task'
   



    def action_send_mail_task_reminder(self):
        print("action triggered")

        today = datetime.today().date()
        start_of_day = datetime.combine(today, time.min)  
        end_of_day = datetime.combine(today, time.max)    


        tasks = self.env['project.task'].search([
            ('date_deadline', '>=', start_of_day),
            ('date_deadline', '<=', end_of_day)
        ])

        
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        print('----------',tasks)



        for task in tasks:
            for assignee in task.user_ids:
                template = self.env.ref('task_reminder.mail_to_user_deadline_template_id', raise_if_not_found=False)
                if template and assignee.email and task.state != "1_done":
                    task_url = f"{base_url}/odoo/all-tasks/{task.id}"
                    email_ctx = {
                        'task_url': task_url,
                        'name': assignee.name,  
                    }
                    email_values = {
                        'email_to': assignee.email,
                        'email_from': self.env.user.email,
                    }
                    template.with_context(email_ctx).send_mail(task.id, force_send=True, email_values=email_values)
                    task.message_post(
                       body="email sent"
                    )
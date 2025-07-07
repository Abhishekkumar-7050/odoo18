from odoo import models, fields,api
from datetime import datetime, timedelta
from datetime import date 
import logging 



_logger = logging.getLogger(__name__)



class Student(models.Model):
    _name = 'student.student'
    _inherit = ['mail.thread', 'mail.activity.mixin',]
    _description = 'Student'
    _rec_name ='name'
    student_id = fields.Integer()
    name = fields.Char(string='Name' , required= True)
    age = fields.Integer(string='Age', required= True)
    Class = fields.Char(string='class', required= True)
    Image = fields.Binary(string = "Photo")
    Email = fields.Char(string ="Email", required= True)
    Birthday = fields.Datetime()
    # creat these fields to implement calender views by default date
    start_date = fields.Datetime(default=lambda self: datetime.now())
    end_date = fields.Datetime(default=lambda self: datetime.now() + timedelta(days=6))


    school_id =  fields.Many2one('school.school')


    # _sql_constraints = [
       
    #     ('name_not_be_empty',
    #      "CHECK(name IS NOT NULL AND name != '')",
    #      'name cannot be empty.'),

    #     ('negative_age',
    #      "CHECK(age IS NOT NULL AND age > 0)",
    #      'age cannot be empty or negative.'),


    #     ('not_be_empty', 
    #      "CHECK(Class != '')", 
    #      'Class cannot be empty or null'),
       
    
    # ]


    def action_send_mail_task(self):
        #   import pdb ;pdb.set_trace()
        records = self.env['student.student'].search([('Email' , '!=' , '')])

        today_date_object = date.today()
    
        today = today_date_object.day
        today_month_object = date.today()
        month = today_month_object.month
        for rec in records:

            if rec.Birthday and rec.Birthday.day == today and  rec.Birthday.month == month:
                template = self.env.ref('my_module.mail_to_student_template_id')
                email_values = {'email_from': self.env.user.email}
                template.send_mail(rec.id, force_send=True, email_values=email_values)
                rec.message_post(body="email sent" 
           
                                                            )
                
    
    def action_send_mail_task_single(self):
       
        template = self.env.ref('my_module.mail_to_student_template_id')
        email_values = {'email_from': self.env.user.email}
        template.send_mail(self.id, force_send=True, email_values=email_values)

        # attachments = template.env['ir.attachment'].browse(template.report_template_ids)
        # print("================================",attachments)


        # self.message_post(subject='Indent Approved',  message_type="notification",
        #                     subtype_xmlid="mail.mt_note", partner_ids=self.issued_by_id.partner_id.ids)
        
        # self.message_post(body="email sent" 
               
        #                                                     )
        # return {'type': 'ir.actions.client',
        #             'tag': 'display_notification',
        #             'params': {
        #                 'title':('Email sent'),
        #                 'sticky': False,
        #         }}
    





    def check_log_button(self):
     _logger.warning("This is my custom warning to check the log button")

    # def take_action(self):
    #    print("Action Done")

    @api.onchange('name')
    def onchange_name(self):
        """ Logging at different levels """
        _logger.debug("------------IT IS DEBUG-----------")
        _logger.info("-------------IT IS INFO------------")
        _logger.error("------------IT IS Error-----------")
        _logger.warning("----------IT IS warning---------")
        _logger.critical("----------IT IS Critical---------")



















    
    # # create a  new record
    # def addRecord(self):
    #    new_record = self.env['student.student'].create({
    #    'name' : 'qqqq',
    #    'age' : 34,
    #    'Class': 'ME'
    # })
    #    print(f"new record created{new_record}")
    
   

    # # search method

    # def searchRecord(self):
    #     self.addRecord()

    #     record = self.env['student.student'].search([
    #     ('name' , '=' ,'qqqq')
    #      ])
    #     print(f'searc record{record}')
    
    

    
   
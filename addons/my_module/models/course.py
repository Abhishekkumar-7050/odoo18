from odoo import models, fields
from datetime import datetime, timedelta

class Course(models.Model):
    _name = 'course.course'
    _rec_name ='Course_name'
    _description = 'courses'
    _order = 'course_id desc'


    course_id =  fields.Integer()
    Course_name = fields.Char(string='Course Name', required=True)
    Department = fields.Char(string='Department Name')
    Duration = fields.Integer(string = "Course Duration in years")
    # creat these fields to implement calender views by default date
    start_date = fields.Datetime(default=lambda self: datetime.now())
    end_date = fields.Datetime(default=lambda self: datetime.now() + timedelta(days=500))


    

    

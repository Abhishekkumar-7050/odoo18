from odoo import models, fields, api
from datetime import time
from odoo.exceptions import ValidationError


class TimeSlot(models.Model):
    _name = "appointment.time_slot"
    _description = "Available Time Slot"
    _order = "day_name"


    name = fields.Char(string = "Slot Name :" ,compute="_compute_name")
    day_name = fields.Selection([
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ], string='Day', required=True)

    start_time = fields.Float(string="Start Time :", required=True)
    end_time = fields.Float(string="End Time :", required=True)

    appointees_id = fields.Many2many('appointment.appointees' , string='Appointee' , required=True)
 


 

    _sql_constraints = [
        ('check_time_range', 'CHECK(start_time <= end_time)', 'Start time must be before end time.')
    ]

    discription = fields.Text(string="Description")

    @api.depends('day_name', 'start_time', 'end_time')
    def _compute_name(self):
        short_days = {
            'monday': 'Mon', 'tuesday': 'Tue', 'wednesday': 'Wed',
            'thursday': 'Thu', 'friday': 'Fri', 'saturday': 'Sat', 'sunday': 'Sun'
        }

        for rec in self:
            if rec.day_name and rec.start_time is not None and rec.end_time is not None:
                start_hour = int(rec.start_time)
                start_min = int((rec.start_time - start_hour) * 60)
                end_hour = int(rec.end_time)
                end_min = int((rec.end_time - end_hour) * 60)

                start_time = f"{start_hour:02d}:{start_min:02d}"
                end_time = f"{end_hour:02d}:{end_min:02d}"
                day = short_days.get(rec.day_name, rec.day_name.capitalize())

                rec.name = f"{day} ({start_time} - {end_time})"
            else:
                rec.name = "-"

    

    @api.constrains('day_name', 'start_time', 'end_time')
    def _check_duplicate_time_slot_on_day(self):
        for rec in self:
            overlap = self.search([
                ('id', '!=', rec.id),
                ('day_name', '=', rec.day_name),
                ('start_time', '<', rec.end_time),
                ('end_time', '>', rec.start_time)
            ])
            if overlap:
                raise ValidationError(
                    f"Time slot on {rec.day_name.capitalize()}  an existing slot."
                )
    


    @api.constrains('start_time', 'end_time')
    def _check_time_constraints(self):
        for rec in self:
            if rec.start_time < 0 or rec.start_time > 23.5:
                raise ValidationError("Start Time must be between 0.0 and 23.5 (i.e., not after 23:30).")

            if rec.end_time > 24:
                raise ValidationError("End Time must not exceed 24:00.")
            
                    
            if round(rec.end_time - rec.start_time, 2) != 0.5:
                raise ValidationError("Appointment must be exactly 30 minutes long.")


          
from odoo import models ,fields , api



class appointmentline(models.Model):
    _name = "appointment.line"

    appointment_for = fields.Char(string = "appointment For")
    description = fields.Char(string = "Description")
    price = fields.Float(string="Unit Price")
    sub_total = fields.Float(string="Sub Total", compute="_compute_sub_total", store=True)
    appointment_id = fields.Many2one('appointment.appointment')

    

    @api.depends('price')
    def _compute_sub_total(self):
        for rec in self:
            rec.sub_total = rec.price



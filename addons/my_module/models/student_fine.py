from odoo import models , api, fields



class Calculate_fine(models.Model):
    _name = 'fine.fine'
    _description = 'Fine Calculation'
    _rec_name = 'leave'

    leave = fields.Integer(string = 'Number of leave' )

    total_fine = fields.Integer( string = "total fine INR :" ,compute='_compute_total_fine')








    @api.depends('leave')
    def  _compute_total_fine(self):

        self.total_fine = self.leave * 10

        







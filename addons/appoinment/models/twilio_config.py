from odoo import models, fields

class TwilioConfig(models.Model):
    _name = 'twilio.config'
    _description = 'Twilio Configuration'
    _rec_name = 'twilio_number'  

    name = fields.Char(string="Configuration Name", required=True)
    account_sid = fields.Char(string="Account SID", required=True)
    auth_token = fields.Char(string="Auth Token", required=True)
    twilio_number = fields.Char(string="Twilio Number", required=True)
    active = fields.Boolean(default=True)

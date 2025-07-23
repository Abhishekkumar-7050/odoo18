from odoo import models, fields
import requests

class TwilioConfig(models.Model):
    _name = 'twilio.config'
    _description = 'Twilio Configuration'
    _rec_name = 'twilio_number'  

    name = fields.Char(string="Configuration Name", required=True)
    account_sid = fields.Char(string="Account SID", required=True)
    auth_token = fields.Char(string="Auth Token", required=True)
    twilio_number = fields.Char(string="Twilio Number", required=True)
    active = fields.Boolean(default=False)




    def action_test_connection(self):
       
        for rec in self:
            url = f"https://api.twilio.com/2010-04-01/Accounts/{rec.account_sid}.json"
            try:
                response = requests.get(url, auth=(rec.account_sid, rec.auth_token))
                if response.status_code == 200:
                    message = "Twilio connection successful!"
                else:
                    message = f"Failed to connect to Twilio Invalid credentials!"
            except Exception as e:
                message = f"Connection error: {str(e)}"

            # Raise notification
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Twilio Connection Test',
                    'message': message,
                    'type': 'success' if response.status_code == 200 else 'danger',
                    'sticky': False,
                }
            }


from odoo import api, models
import requests

class AppointmentSMS(models.Model):
    _name = 'appointment.appointment'
    _inherit = 'appointment.appointment'

    @api.model
    def send_sms_via_twilio(self):
        config = self.env['twilio.config'].search([('active', '=', True)], limit=1)

        if not config:
            raise ValueError("Twilio configuration not found. Please set it up in the settings.")

         
        for record in self:
           
            account_sid = config.account_sid
            auth_token = config.auth_token
            twilio_number = config.twilio_number

            # Phone number and message
            to_number = record.partner_id.mobile or '+917465057050' 
            print("========", to_number)
            message_body = f"Hello, {record.partner_id.name} your appointment is confirmed. with Appointee {record.appointees_id.name} Ref - {record.name} On Date: {record.appoinnment_date} Time Slot : {record.time_slot_id.name}"

            if to_number:
                url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json"
                payload = {
                    'To': to_number,
                    'From': twilio_number,
                    'Body': message_body,
                }
                auth = (account_sid, auth_token)
                response = requests.post(url, data=payload, auth=auth)

                if response.status_code in (200, 201):
                    print("SMS sent successfully to", to_number)
                else:
                    print("Failed to send SMS:", response.text)
            else:
                print("No phone number found for record:", record.id)

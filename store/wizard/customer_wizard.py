from odoo import models, fields, api
import logging

_logger = logging.getLogger("My Custom Logger")


class Customer(models.TransientModel):
    _name = 'customer_wizard'

    first_name =  fields.Char(string= 'First Name')






    def button_confirm(self):
        context = self.env.context


        customer_rec_id =  context.get('active_id', False)

        record = self.env[context.get('active_model' , False)].browse(customer_rec_id)

        # record.first_name.id = self.id

        record.first_name = self.first_name


        _logger.info(f'==={record.first_name }===={record}========{ self.first_name}======================')



    







from odoo import models, fields, api
import logging

_logger = logging.getLogger("My Custom Logger")


class Order(models.TransientModel):
    _name = 'order.wizard'

    customer_id = fields.Many2one('customer.customer', 'customer')

    def button_confirm(self):
        context = self.env.context

        # customer_user_rec_id =  context.get('customer_rec_id', False)

        # record = self.env['order.wizard'].browse(customer_user_rec_id)

        # record.customer_id = self.customer_id.id


        customer_user_rec_id =  context.get('active_id', False)

        record = self.env[context.get('active_model' , False)].browse(customer_user_rec_id)

        record.customer_id = self.customer_id.id
        





        _logger.info(f'======={record.customer_id}========{ self.customer_id.id}======================')


     
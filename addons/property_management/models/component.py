from odoo import models, fields, api

class Components(models.Model):
    _name = 'component.component'
    _description = 'Components'

    name = fields.Char(required=True)

    def action_add_to_property_room(self):
        pass
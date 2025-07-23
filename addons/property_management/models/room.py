from odoo import models, fields

class RoomComponentLine(models.Model):
    _name = 'room.component.line'
    _description = 'Room Component Lines'

    component_id = fields.Many2one('component.component', string="Component")
    room_line_id = fields.Many2one('property.room.line', string="Room Line")
    length = fields.Float()
    height = fields.Float()
    

class Room(models.Model):
    _name = 'room.room'
    _description = 'Room'

    name = fields.Char(required=True)






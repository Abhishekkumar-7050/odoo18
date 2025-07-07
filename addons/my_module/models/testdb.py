from odoo  import models , fields 



class Car(models.Model):
    _name = "cars"
    _description = 'cars'
    id = fields.Integer()
    brand = fields.Char(string= "Car_name")
    model = fields.Char(string= "Model_name")
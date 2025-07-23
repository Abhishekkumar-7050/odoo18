from odoo import models, fields ,api 
from odoo.exceptions import ValidationError
from datetime import date, timedelta ,datetime
from odoo.exceptions import UserError




class appointment(models.Model):
    _name ="appointment.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(
        string="Order Reference",
        required=True, copy=False, readonly=False,
        index='trigram',
        default=lambda self:('New'))
    

    "'overrides the create method to create the  refrence number'"
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', "New") == "New":
                year = datetime.now().year
                ctx = dict(self.env.context or {}, year=year)
                vals['name'] = self.env['ir.sequence'].with_context(ctx).next_by_code(
                    'appointment.appointment'
                ) or "New"
            vals['state'] = "pending"
        return super().create(vals_list)


    partner_id = fields.Many2one(
            'res.partner',
            string="Customer",
            required=True
        )
    

    street = fields.Char(related='partner_id.street', store=False)
    city = fields.Char(related='partner_id.city', store=False)
    zip = fields.Char(related='partner_id.zip', store=False)
    phone = fields.Char(related='partner_id.phone', store=False)
    email = fields.Char(related='partner_id.email', store=False)

    
    appoinnment_date = fields.Date(
    string="Appointment Date",
    required=True,
    help="Choose the appointment date. It must be after the create date."
     )

    create_date = fields.Date(
        string="Create Date",
        required=True,
        default=fields.Date.context_today,
        help="The date this appointment is created. It must not be in the past."
    )

    state = fields.Selection([
        ('new', 'New'),
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='new', tracking=True)

    appointees_id = fields.Many2one('appointment.appointees', string='Appointees', required=True)


    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id , string = "Pricelist")



    "'fetch all group in which apoointees is  group member appintees_ids in group  appointees_id in the appointment'"

    order_line = fields.Many2many(
        comodel_name='appointment.group',
        inverse_name='appointment_ids',
        string="Order Lines",
        domain="[('appointees_ids', 'in', [appointees_id])]" 
    )


    discription =  fields.Text()


    # description_line = fields.Char(string = "Description")

    amount_untaxed = fields.Monetary(string="Untaxed Amount", compute="_compute_amount", store=True)
    amount_tax = fields.Monetary(string="Taxes", compute="_compute_amount", store=True)
    amount_total = fields.Monetary(string="Total", compute="_compute_amount", store=True)
    

    day_name = fields.Selection([
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ], compute='_compute_day_name', store=True)

    
    reject_resson = fields.Char()
    detailed_discription = fields.Text(string = "Purpose of Appointment")

    "'computing the  day name by appointment day'"
    @api.depends('appoinnment_date')
    def _compute_day_name(self):
        for rec in self:
            if rec.appoinnment_date:
                rec.day_name = rec.appoinnment_date.strftime('%A').lower()



    "'Filters the dropdown to only show records whose id is in the time_slot_ids list.'"
    time_slot_id = fields.Many2one(
    'appointment.time_slot',
    string='Time Slot',
    domain="[('id', 'in', time_slot_ids)]",
    required=True
     )
    
    "' Fetching the  time slots computed by day name  for the particular Appoitees'"
    time_slot_ids = fields.Many2many(
    'appointment.time_slot',
    compute='_compute_time_slot_ids',
    string='Available Slots'
    )
    
    reject_resson = fields.Char()
    detailed_discription = fields.Text(string = "Purpose of Appointment")



    "'compute field  filtering the time slots of the current appointees on a day name of appointment date'"
    @api.depends('appointees_id', 'day_name')
    def _compute_time_slot_ids(self):
        for rec in self:
            if rec.appointees_id and rec.day_name:
                slots = rec.appointees_id.time_slot_line.filtered(lambda s: s.day_name == rec.day_name)
                rec.time_slot_ids = slots
            else:
                rec.time_slot_ids = [(5, 0, 0)]


    # Button actions
    def action_set_pending(self):
        for rec in self:
            rec.state = 'pending'

   
    def action_approve(self):
        for rec in self:
      
            rec.write({'state': 'approved'})
            template = self.env.ref('appoinment.appointment_email_template_approved', raise_if_not_found=False)
            if template and rec.partner_id.email:
                template.send_mail(rec.id, force_send=True)


    def action_reject(self):
        for rec in self:
          
            rec.write({'state': 'rejected'})
            template = self.env.ref('appoinment.appointment_email_template_rejected',raise_if_not_found=False)
            if template and rec.partner_id.email:
                template.send_mail(rec.id, force_send=True)

    

      

    @api.constrains('create_date', 'appoinnment_date')
    def _check_create_before_appointment(self):
        for rec in self:
            if rec.create_date and rec.appoinnment_date:
                if rec.create_date > rec.appoinnment_date:
                    raise ValidationError("Create Date cannot be after the Appointment Date.")

    
    

    "'compute the total amount and sub total'"
    @api.depends('order_line.appointment_charge')
    def _compute_amount(self):
        for order in self:
            untaxed = 0.0
            tax = 0.0
            for line in order.order_line:
                 untaxed += line.appointment_charge
               
            order.amount_untaxed = untaxed
            order.amount_tax = tax
            order.amount_total = untaxed + tax


    #     # Prevent double booking
    # @api.constrains('appointees_id', 'time_slot_id', 'appoinnment_date')
    # def _check_double_booking(self):
    #     for rec in self:
    #         domain = [
    #             ('appointees_id', '=', rec.appointees_id.id),
    #             ('time_slot_id', '=', rec.time_slot_id.id),
    #             ('appoinnment_date', '=', rec.appoinnment_date),
    #             ('id', '!=', rec.id),
    #         ]
    #         if self.search_count(domain):
    #             raise ValidationError(("This time slot is already booked for the selected appointee on the same day."))
      

    

    "'check availablity and prevent the double booking'"
    @api.constrains('appointees_id', 'appoinnment_date', 'time_slot_id')
    def _check_time_slot_availability(self):
        for rec in self:
            if not rec.appointees_id or not rec.appoinnment_date or not rec.time_slot_id:
                continue

            # Ensure slot belongs to that day of week
            if rec.time_slot_id.day_name != rec.day_name:
                raise ValidationError("Selected time slot does not match the appointment day.")

            # Check if already booked
            existing = self.search([
                ('id', '!=', rec.id),
                ('appointees_id', '=', rec.appointees_id.id),
                ('appoinnment_date', '=', rec.appoinnment_date),
                ('time_slot_id', '=', rec.time_slot_id.id),
            ])
            if existing:
                raise ValidationError("This time slot is already booked for the selected appointee on this date.")
            
    

    "'contrains  for create date must be at least on day before appointment date'"
    @api.constrains('appoinnment_date', 'create_date')
    def _check_dates(self):
        for rec in self:
            today = date.today()
            if rec.appoinnment_date and rec.appoinnment_date < today:
                raise ValidationError("Appointment date cannot be in the past.")

            if rec.create_date and rec.create_date < today:
                raise ValidationError("Create date cannot be in the past.")

            if rec.appoinnment_date and rec.create_date:
                if rec.appoinnment_date <= rec.create_date:
                    raise ValidationError("Appointment date must be at least the next day of the create date.")
                

    
    
    invoice_id = fields.Many2one('account.move', string='Invoice', readonly=True, copy=False)

    def action_create_invoice(self):
        for appointment in self:
            if appointment.invoice_id:
                raise UserError("Invoice already created.")

            if not appointment.partner_id:
                raise UserError("Please set a customer.")

            if not appointment.order_line:
                raise UserError("Please add at least one service line to invoice.")

            
            invoice_lines = []
            for group in appointment.order_line:
                 invoice_lines.append((0, 0, {
                'name': group.group_name or 'Group Charge',
                'quantity': 1.0,
                'price_unit': group.appointment_charge,
                
           
            }))

        invoice_vals = {
            'move_type': 'out_invoice',
            'partner_id': appointment.partner_id.id,
            'invoice_origin': f"Appointment {appointment.name or appointment.id}",
            'invoice_date': fields.Date.today(),
            'invoice_line_ids': invoice_lines,
        }

        invoice = self.env['account.move'].create(invoice_vals)
        appointment.invoice_id = invoice.id

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'res_id': invoice.id,
            'view_mode': 'form',
            'target': 'current',
        }
    
    def action_for_invoice(self):
            return {
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'res_id': self.invoice_id.id,
            'view_mode': 'form',
            'target': 'current',
        }

                
    def action_reject_wizard(self):
        
            return {
                'name': ' Reject Reason',
                'type': 'ir.actions.act_window',
                'view_mode' : 'form',
                'res_model' : 'appointment.reject',
                'target':'new',
                
            }
    
    
    


  







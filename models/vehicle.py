from odoo import models, fields, _, api
from odoo.exceptions import ValidationError
from datetime import date

class Vehicle(models.Model) :
    _name = "mini.vehicle"
    _description = "Registre de Véhicules"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="License Plate", required=True)
    brand = fields.Char(string="Brand", required=True)
    model = fields.Char(string="Model", required=True)
    year = fields.Integer(string="Year")
    color = fields.Char(string="Color")
    chassis_no = fields.Char(string="Chassis number", required=True)
    mileage = fields.Integer(string="Mileage")

    log_ids = fields.One2many('mini.vehicle.log', 'vehicle_id', string="Vehicle Logs")

    driver_id = fields.Many2one(
        'res.partner', 
        string='Driver', 
        ondelete='set null', 
        help='Select the driver of this vehicle'
    )

    @api.constrains('mileage')
    def _check_mileage(self):
        for record in self:
            if record.mileage < 0 or record.mileage > 2000000:
                raise ValidationError("Le kilométrage doit etre compris entre 0 et 2 000 000 km.")

    @api.constrains('year')
    def _check_year(self):
        current_year = date.today().year
        for record in self:
            if record.year :
                if record.year < 1900 or record.year > current_year + 1:
                    raise ValidationError(f"L'année doit être compris entre 1900 et {current_year + 1}.")

    driver_phone = fields.Char(related='driver_id.phone', string="Driver\'s phone", readonly=True)

    state = fields.Selection([
        ('draft', _('Draft')),
        ('stock', _('In stock')),
        ('running', _('Running')),
        ('rental', _('Rental')),
        ('sold', _('Sold'))
    ], string='Statut', default='draft', tracking=True, required=True)

    def action_set_stock(self):
        for record in self:
            record.state = 'stock'

    def action_set_running(self):
        for record in self:
            record.state = 'running'
    
    def action_set_rental(self):
        for record in self:
            record.state = 'rental'
    
    def action_set_sold(self):
        for record in self:
            record.state = 'sold'

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'This license plate already exists.'),
        ('chassis_no_unique', 'UNIQUE(chassis_no)', 'This chassis number already exists.')
    ]

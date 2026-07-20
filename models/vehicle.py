from odoo import models, fields, _

class Vehicle(models.Model) :
    _name = "mini.vehicle"
    _description = "Registre de Véhicules"

    name = fields.Char(string="License Plate", required=True)
    brand = fields.Char(string="Brand", required=True)
    model = fields.Char(string="Model", required=True)
    year = fields.Integer(string="Year")
    color = fields.Char(string="Color")
    chassis_no = fields.Char(string="Chassis number", required=True)
    mileage = fields.Float(string="Mileage")

    log_ids = fields.One2many('mini.vehicle.log', 'vehicle_id', string="Vehicle Logs")

    driver_id = fields.Many2one(
        'res.partner', 
        string='Driver', 
        ondelete='set null', 
        help='Select the driver of this vehicle'
    )

    driver_name = fields.Char(related='driver_id.name', string=_("Driver name"), readonly=True)
    driver_phone = fields.Char(related='driver_id.phone', string=_("Driver\'s phone"), readonly=True)

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
        ('name_unique', 'UNIQUE(name)', _('This license plate already exists.')),
        ('chassis_no_unique', 'UNIQUE(chassis_no)', _('This chassis number already exists.'))
    ]

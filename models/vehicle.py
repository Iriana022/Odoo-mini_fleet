from odoo import models, fields, _

class Vehicle(models.Model) :
    _name = "mini.vehicle"
    _description = "Registre de Véhicules"

    name = fields.Char(string='License Plate', required=True)
    brand = fields.Char(string='Brand', required=True)
    model = fields.Char(string="Model", required=True)
    year = fields.Integer(string="Year")
    color = fields.Char(string="Color")
    chassis_no = fields.Char(string="Chassis number", required=True)
    mileage = fields.Float(string="Mileage")

    driver_id = fields.Many2one(
        'res.partner', 
        string='Driver', 
        ondelete='set null', 
        help='Select the driver of this vehicle'
    )

    state = fields.Selection([
        ('draft', 'Nouveau'),
        ('runing', 'En service'),
        ('maintenance', 'En maintenance'),
        ('Archived', 'Réformé')
    ], string='Statut', default='draft', tracking=True)

    def action_set_running(self):
        for record in self:
            record.state = 'runing'
    
    def action_set_maintenance(self):
        for record in self:
            record.state = 'maintenance'

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', _('This license plate already exists.')),
        ('chassis_no_unique', 'UNIQUE(chassis_no)', _('This chassis number already exists.'))
    ]

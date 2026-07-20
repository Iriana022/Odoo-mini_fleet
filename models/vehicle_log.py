from odoo import models, fields

class VehicleLog(models.Model):
    _name = "mini.vehicle.log"
    _description = "Historique des véhicules"
    _order = "date desc"

    name = fields.Char(string="Description", required=True)
    date = fields.Date(string="Date", default=fields.Date.context_today, required=True)
    vehicle_id = fields.Many2one('mini.vehicle', string="Véhicule", required=True, ondelete='cascade')
    note = fields.Text(string="Notes")
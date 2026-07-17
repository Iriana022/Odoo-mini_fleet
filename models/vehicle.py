from odoo import models, fields

class Vehicle(models.Model) :
    _name = "mini.vehicle"
    _description = "Registre de Véhicules"

    name = fields.Char(string='Immatriculation', required=True)
    brand = fields.Char(string='Marque', required=True)
    model = fields.Char(string="Modèle", required=True)
    year = fields.Integer(string="Année")
    color = fields.Char(string="Couleur")
    chassis_no = fields.Char(string="Numéro de châssis", required=True)
    mileage = fields.Float(string="Kilométrage actuel")


    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Ce numéro d\'immatriculation existe déjà.'),
        ('chassis_no_unique', 'UNIQUE(chassis_no)', 'Ce numéro de châssis existe déjà.')
    ]
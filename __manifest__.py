{
    'name': 'Mini fleet',
    'version': '1.0',
    'summary': 'Pour gérer un registre de véhicules d\'entreprise. Chaque véhicule est identifié par son numéro de châssis, notion directement transposable au concept de numéro de lot dans Odoo Stock.',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/vehicle_views.xml',
        'views/menu.xml'
    ],
    'installable': True,
    'application': True,
}
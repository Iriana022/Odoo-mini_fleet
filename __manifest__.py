{
    'name': 'Mini fleet',
    'version': '16.0.1.0.0',
    'category' : 'Fleet Management',
    'author': 'Iriana R / Materauto',
    'license': 'LGPL-3',
    'summary': 'Pour gérer un registre de véhicules d\'entreprise. Chaque véhicule est identifié par son numéro de châssis, notion directement transposable au concept de numéro de lot dans Odoo Stock.',
    'depends': ['base', 'contacts', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/vehicle_views.xml',
        'views/menu.xml'
    ],
    'demo': [
        'data/demo_data.xml'
    ],
    'installable': True,
    'application': True,
}
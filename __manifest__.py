{
    'name': 'Optica Vision',
    'version': '1.2',
    'category': 'Sales/CRM',
    'sequence': 15,
    'summary': 'Track leads and close opportunities',
    'description': "",
    'website': 'https://www.odoo.com/page/crm',
    'depends': ['base', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/optica_revision_views.xml',
        'views/optica_tienda_views.xml',
        'views/optica_dia_views.xml',
        'views/optica_garantia_views.xml',
        'views/optica_reparacion_views.xml',
        'views/optica_reemplazo_views.xml',
        'views/optica_menus.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}
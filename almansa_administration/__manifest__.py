{
    'name': 'Almansa_administration',
    'summary': """Administration settings for Almansa Santos""",
    'version': '13.0.1.0.0',
    'description': """Administration settings for Almansa Santos""",
    'author': 'DDL-Xtendoo',
    'company': 'Xtendoo',
    'website': 'http://xtendoo.es',
    'category': 'Admin Tools',
    'depends': [
        'base',
        'sale',
        'sale_margin',
        'sale_order_margin_percent',
        'sale_order_line_margin_percent'
    ],
    'license': 'AGPL-3',
    'data': [
        'views/sale_order_views.xml',
        'views/sale_order_line_views.xml',
        'security/security_group.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': True,
}

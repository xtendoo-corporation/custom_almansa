{
    'name': 'Sale order line product tree view',
    'summary': """Sale order line product tree view""",
    'version': '13.0.1.0.0',
    'description': """Administration settings for Almansa Santos""",
    'author': 'Dani Domínguez',
    'company': 'Xtendoo',
    'website': 'http://xtendoo.es',
    'category': 'Admin Tools',
    'depends': [
        'base',
        'sale',
        'stock',
    ],
    'license': 'AGPL-3',
    'data': [
        'views/sale_order_line_views.xml',
        'views/stock_quant_views.xml',
    ],
    'installable': True,
    'auto_install': True,
}

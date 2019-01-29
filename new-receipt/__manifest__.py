
{
    'name': 'Odoo New Reciept',
    'summary': """new fancy reciept for odoo pos ticket""",
    'version': '1.0',
    'description': """new fancy reciept for odoo pos ticket""",
    'author': 'ITSS',
    'company': 'integrated Technical software Solutions',
    'website': 'www.itss-c.com',
    'category': 'Point Of Sale',
    'depends': ['base', 'point_of_sale'],
    'license': 'LGPL-3',
    'data': [         
        'views/views.xml',
        'views/templates.xml',
        ],
    'qweb': ['static/src/xml/pos_ticket_view.xml'],
    'demo': [],
    'installable': True,
    'auto_install': False,
}

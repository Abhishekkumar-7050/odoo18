# -*- coding: utf-8 -*-
{
    'name': 'Store Management',
    'version': '1.0',
    'summary': 'Manage store and order',
    'category': 'Sale',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
         'security/ir.model.access.csv',
         'wizard/customer_wizard.xml',
         'views/order_view.xml',
         'views/customer_view.xml', 
         'wizard/order_wizard.xml',
    ],
    'installable': True,
    'application': True,
}

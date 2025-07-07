
{
    'name': 'Po 3-Level Approval',
    'version': '1.0',
    'summary': 'Manage store and order',
    'category': 'purchase',
    'author': 'Your Name',
    'depends': ['purchase', 'base', 'mail'],
    'data': [
         'security/ir.model.access.csv',
         'security/security.xml',
         'data/mail_template_data.xml',
         'data/manager_email_actions.xml',
         'wizard/refuse_wizard.xml',
         'views/company_views.xml',
         'views/purchase_order_view.xml',

    ],
    'installable': True,
    'application': True,
}

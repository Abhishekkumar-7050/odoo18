# -*- coding: utf-8 -*-
{
    'name': 'appointment',
    'version': '1.0',
    'summary': 'appointment',
    'category': 'Management',
    'author': 'Your Name',
    'depends': ['base','sale'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/ir.sequence.xml',
        'data/reject__approved_email_template.xml',
        'wizard/reject_wizard.xml',
        'views/twilio_sms_gateway_view.xml',
        'views/appointment_view.xml',
        'views/apointees_view.xml',
        'views/reports_view.xml',
        'views/time_slot_view.xml',
        'views/dashboard.xml',
        'views/appoitment_group.xml',
    ],

  'assets': {
    'web.assets_backend': [
        'appoinment/static/src/js/dashboard.js',
        'appoinment/static/src/xml/dashboard.xml',
    ],
  },

    'installable': True,
    'application': True,
}

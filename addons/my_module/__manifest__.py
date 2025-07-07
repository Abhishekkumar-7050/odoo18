# -*- coding: utf-8 -*-
{
    'name': 'Student Management',
    'version': '1.0',
    'summary': 'Manage students with name and age',
    'category': 'Education',
    'author': 'Your Name',
    'depends': ['base','sale','mail','contacts', 'website'],
    'data': [
     #     'data/student_data.xml',
         'data/student.student.csv',
         'security/ir.model.access.csv',
         'security/security.xml',
         'views/student_views.xml',
         'views/newbtn_view.xml',
         'views/odoo_services.xml',
         'views/student_fine_view.xml',
         'views/library_view.xml',
         'views/course_view.xml',
         'views/school_view.xml',
         'views/testdb_views.xml',
         'views/patient_view.xml',
        #  'views/patient_web_view.xml',
         'reports/quotation_report.xml',
         'reports/quotation_report_template.xml',
         'reports/report_email_pdf_template.xml',
         'reports/action_email_pdf.xml',
         'views/sales_order.xml',
         'data/ir_action_data.xml',
         'data/mail_template_data.xml',
         'data/contact_us.xml',
    ],

    'assets': {
    'web.assets_frontend': [ 
        #  'my_module/static/src/component/patient_list.js',
        #  'my_module/static/src/component/orm_call.js',
        #  'my_module/static/src/xml/patient_form.xml',
        #  'my_module/static/src/xml/patient_list_template.xml',
        #  "my_module/static/src/js/rpc_method.js"

    ],
     'web.assets_backend': [
         'my_module/static/src/component/orm_call.js',
         'my_module/static/src/component/orm_call.xml',
         'my_module/static/src/component/newbtn/newbtn.js',
         'my_module/static/src/component/newbtn/newbtn.xml',
         'my_module/static/src/component/newbtn/newbtn_form.js',
         'my_module/static/src/component/newbtn/newbtn_form.xml',
         'my_module/static/src/component/newbtn/newbtn_kanban.js',
         'my_module/static/src/component/newbtn/newbtn_kanban.xml',
         'my_module/static/src/component/newbtn/newbtn_product.xml',
         'my_module/static/src/component/newbtn/newbtn_product.js',
         

    ],
    },

    


    'installable': True,
    'application': True,
}

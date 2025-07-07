from odoo import http
from odoo.http  import request
import json



class ContactUs(http.Controller):
    @http.route('/student/form', type='http', csrf=False, website= True) 
    def handleform(self , **kwarg):
        # import pdb; pdb.set_trace()
        try:
             studet =  request.env['student.student'].sudo().create({
                'name' : kwarg.get('name'),
                'Email' : kwarg.get('email'),
                'age' : kwarg.get('age'),
                'Class': kwarg.get('Class'),
            })
             return request.redirect('/contactus-thank-you')

        except Exception as e:
            return json.dumps({"message": "Cannot student created",'success': False, 'error': str(e) })

        


   
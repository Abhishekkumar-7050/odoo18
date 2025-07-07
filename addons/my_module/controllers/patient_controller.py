from odoo import http
from odoo.http import request
import base64
import json


class Patientform(http.Controller):
    @http.route('/patient' , type = 'http' , csrf =False, website= True )
    def patient_form_redirect(self , **kw):
    
        try:
            if request.httprequest.method == 'POST':
                name = kw.get('name')
               

                email = kw.get('email')
                email_exists = request.env['patient.patient'].sudo().search([('email' ,'=' ,email)])
                if email_exists.id :
                    name = request.env.user.name
                    email = request.env.user.email
                    phone = request.env.user.phone
                    company = request.env['res.company'].sudo().search([])
                    return request.render('my_module.patient_template',{
                    "exists" : True,
                     'name': name,
                     'email': email,
                     'phone': phone,
                     'company':company
                    
                })
                else :
                    image = request.httprequest.files.get('image').read()
                    image1 = base64.b64encode(image)
                    request.env['patient.patient'].sudo().create({
                    'name' : kw.get('name'),
                    'email' : kw.get('email'),
                    'dob' : kw.get('dob'),
                    'age' : kw.get('age'),
                    'number': kw.get('number'),
                    'gender' : kw.get('gender'),
                    'company': kw.get('company'),
                    'image' :  image1,
                    
            })
               
                return request.render('my_module.patient_template',{
                    "success" : True,
                    "name" : name,
                    
                })
            else:
                # import pdb ; pdb.set_trace()
                    name = request.env.user.name
                    email = request.env.user.email
                    phone = request.env.user.phone
                    company = request.env['res.company'].sudo().search([])

                    values = {
                            'name': name,
                            'email': email,
                            'phone': phone,
                            'company':company

                            }
                    
            return request.render('my_module.patient_template', values)

        except Exception as e:
             return json.dumps({"message": "Cannot student created",'success': False, 'error': str(e) })
        
        
    # @http.route('/patient/submit' , type = 'http' , csrf =False, website= True )
    # def patient_form_submit (self , **kw):
    
    #     try:
    #         # import pdb ; pdb.set_trace()
    #         patient =  request.env['patient.patient'].sudo().create({
    #             'name' : kw.get('name'),
    #             'email' : kw.get('email'),
    #             'dob' : kw.get('dob'),
    #             'age' : kw.get('age'),
    #             'number': kw.get('number'),
    #             'gender' : kw.get('gender'),
    #             'company': kw.get('company')
                

    #         })
           
    #         return request.redirect('/patient')

        
    #     except Exception as e:
    #          return json.dumps({"message": "Cannot student created",'success': False, 'error': str(e) })
        

 


    @http.route('/patient/data' , type = 'http', csrf =False, website= True )
    def handle_patien_data(self , *kw):
        try:
        #  import pdb; pdb.set_trace()
         patient = request.env['patient.patient'].sudo().search([])

        #  print("patient/data",patient.id)

        #  for record in patient:
             
        #      record['image_bytes'] = self.base64_to_image(record.to_store_basestring)
             
             
         return request.render('my_module.patient_data' , {"patient": patient})
        
        except Exception as e:
            return {
                "error" : str(e)
            }
        


    @http.route('/patient/data/rpc' , type = 'json', csrf =False, website= True )
    def get_patien_data(self , *kw):
        try:
        #  import pdb; pdb.set_trace()
         return request.env['patient.patient'].sudo().search([])

     
        
        except Exception as e:
            return {
                "error" : str(e)
            }

          

    
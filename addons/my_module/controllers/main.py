from odoo import http
import json
from odoo.http  import request


class OdooAPIController(http.Controller):
    @http.route('/api/load', type='http',methods = ['GET'], auth='public')
    def api_endpoint(self, **kw):
        # import pdb; pdb.set_trace()
        # Access the request parameters
        parameters = json.loads(http.request.httprequest.data)
        # Process the API request and return the response
        response = {
            'status': 'success',
            'message': 'API request received without authentication',
            'data': {
                'parameters': parameters
            }
        }
        return "<h1> hii there </h1>"
    


#retrive the partners in sales
    @http.route('/get/partner', type='json',methods = ['GET'], auth='user')
    def get_partner(self , **kw):

        try:
            partenr =  request.env['res.partner'].search([])

            return {
                "partners": partenr
            }
            
        except Exception as e:
            return {
                "message": str(e)
            }

    

    @http.route('/api/partners', type='json',methods = ['GET'], auth='public')
    def search_partner(self, **kw):
        # import pdb; pdb.set_trace()
        partner = http.request.env['res.partner'].search([])


        # Access the request parameters
        parameters = json.loads(http.request.httprequest.data)
        # Process the API request and return the response
        response = {
            'status': 'success',
            'message': 'API request received without authentication',
            'data': {
                'parameters': parameters
            },
            'partners': partner
        }
        return response
    


    @http.route('/api/partner/create', type='json', methods = ['POST'], auth='user')
    def create_student(self, **kw):
        # Access the request parameters
        try:
            data = json.loads(http.request.httprequest.data)
            student = http.request.env['student.student'].create(data)
            # parameters = json.loads(http.request.httprequest.data)
            # Process the API request and return the response
            print(data)
            response = {
                'status': 'success',
                'message': ' student created',
                'data': {
                    'parameters': data
                },
                'student': student
            }
            return response
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
        


    
    @http.route( '/route/' , type = 'json' , auth= 'public' ) 
    def   search_student( self, **kwargs ):
        # key1 = kwargs.get('key1' )
        # key2= kwargs.get( 'key2' )
        # import pdb; pdb.set_trace()

        # print(kwargs)
        student = http.request.env['student.student'].search([])

        key2= http.request.httprequest.json

        print( key2["key2"])
        # Your processing logic here

        return {
            "key1" : key2,
            "student": student
        }
            

    @http.route('/api/student/<int:student_id>', type='json', methods=['DELETE'], auth='public')
    def delete_student(self, student_id, **kw):
        try:
            
            student = http.request.env['student.student'].browse(student_id)
            if not student.exists():
                return {'status': 'error', 'message': f'Student with ID {student_id}.'}

            student_name = student.name 
            
            student.unlink()

            return {
                'status': 'success',
                'message': f'Student "{student_name}" (ID: {student_id}) deleted '
            }
        except Exception as e:
            return {'status': 'error', 'message': str(e)}




    @http.route('/api/student/<int:student_id>', type='json', methods=['PUT'], auth='public')
    def update_student_put(self, student_id, **kw):
        try:
            data = json.loads(http.request.httprequest.data)
            
            #  update 
            student = http.request.env['student.student'].browse(student_id)
            if not student.exists():
                return {'status': 'error', 'message': f'Student with ID {student_id} '}

            student.write(data)

            return {
                'status': 'success',
                'message': f'Student with ID {student_id} updated successfully.',
                'data': {
                    'student_id': student.id,
                    'student_name': student.name,
                }
            }
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
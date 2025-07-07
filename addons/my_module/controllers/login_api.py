from odoo import http
from odoo.http  import request
import json




class odooApiLoginController(http.Controller):
    @http.route('/login/authenticate', type='http', auth="user",
            methods=['POST'] , csrf= False)
    def get_token(self, **kwargs):
        
        # import pdb; pdb.set_trace()
        login = kwargs.get('username')
        password =kwargs.get('password')
        print(login , password)

        
        try:
            if login == "":
                return json.dumps({"message": "username cannot be empty"})
            
            if password == "":
                return json.dumps({ "message": "password cannot be empty"})


            user_login = request.env['res.users'].sudo().search([('login' , '=' , login)])
            print(user_login , user_login.id)
            if   user_login.id:
                credentials ={"login": login ,"password": password , 'type' :'password'}
                userid = request.session.authenticate(request.db, credentials)
                print("what is this",userid)
                user = request.env['res.users'].browse(userid["uid"])

                print("password", user.login)
                if user :
                    return json.dumps({'message':"Logged in successfully ",'success': True,'user_id': user.id , 'status':"200"})
                else:
                    return json.dumps({'success': False, 'error': 'Invalid credentials'})
            else :
                return json.dumps({'message':"Invalid username",'success': False,'userid': user_login.id, 'status':"401"})

        except Exception as e:
            
            return json.dumps({"message": "INVALID Password",'success': False, 'error': str(e) , 'status' : "401"})

        

    



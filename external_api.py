import xmlrpc.client
url = 'http://localhost:8012'
db = 'newdb'
username = 'admin'
password = 'admin'
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print("version info",common.version())
uid = common.authenticate(db, username, password, {})

if uid:
   print("Authentication success" , uid)


models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

count = models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[['is_company', '=', True]]])
print("count" , count)

ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]], {'offset': 10, 'limit': 5})

print("partner " , ids)
records = models.execute_kw(db, uid, password, 'res.partner', 'read', [ids], {'fields': ['name', 'country_id', 'comment']})

print("records data" , records)

# search read method 

rec = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', True]]], {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
print("search_ read", rec )

# create method
id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': "New Partner"}])
print("new created record", id)

# update the  record

models.execute_kw(db, uid, password, 'res.partner', 'write', [[id], {'name': "Newer partner"}])
# get record name after having changed it
updated_rec = models.execute_kw(db, uid, password, 'res.partner', 'read', [[id], ['display_name']])

print("updated record " , updated_rec)

# delete the above record 
models.execute_kw(db, uid, password, 'res.partner', 'unlink', [[id]])
# check if the deleted record is still in the database
result = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['id', '=', id]]])

print(result)
 




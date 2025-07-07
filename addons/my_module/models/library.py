from odoo import models , fields , api

import logging

_logger = logging.getLogger("My Custom Logger")


class Library(models.Model):
    _name = "library.library"
    _rec_name = 'name'
    _description = 'library'

    name = fields.Char(required = True ,string="Book Name")
    author = fields.Char(string= "Author Name")



    # many books could have 

    relation_book_student =  fields.Many2many('student.student','student_book_relation','name','student_id',string='student_book_ relation')





    
    def add_record(self):
        self.env['library.library'].create({
          'name' : "the art",
          'author' : 'robert',
        })
        _logger.info("========== field created by custom orm ===================")
        
    # serch on certain condition
    def search_record (self):
        records = self.env['library.library'].search([('name', '=', 'boookii'), ('id' , '=', '1')])
        _logger.info( f'==============record serch {records}=============')


    def search_record(self):
        # records = self.env['customers'].search([])
        # records = self.env['customers'].search([('age','>','25')])
        records = self.env['library.library'].search([],limit=2, offset=2, order="name desc")

        _logger.info(records)

        for record in records:
            _logger.info(f"{record.first_name},{record.age}")

    

    # def search_bycontext(self):
           
    #     books = self.env['library.library'].search([('name' ,'in' , [self.env.context.get('name' , 'author' , '')]),])

    #     _logger.info(f'=============== search context {books}  ')

    #     return books

           




 # refrence 
# roduct_ids self.env['sale.order.line'].search([
#             ('order_id', 'in', [self.env.context.get('order_id', '')]),
#         ]).product_id.ids
#         return [('id', 'in', product_ids)]



    # same search count return
    def search_record (self):
        records = self.env['library.library'].search_count([('name', '=', 'boookii')])
        _logger.info( f'==============record serch {records}=============')

    # search specified field
    def  search_sepecified_field(self):
         record = self.read(['name' ,'author'])
         record.name
         record.name

         _logger.info(f'=======record specified record {record}=========') 
    
    # copy record
    def copy_record(self):
        copy_record =  self.copy()
       

     # delete existing record 
    def delete_record(self):
        # record = self.env('library.library').browse(self.id)
        record = self.env['library.library'].search([('name', '=', 'boookii')])
        _logger.info(f'=============deleted field {record} =======================')
        record.unlink()


    # update existing  records
    def write_record(self):
        
        self.write({'name':'update_name_by_orm'})
  

    # sort orm 

    def sort_field(self):
        book = self.env['library.library'].search([])

        book_list = book.sorted(key = lambda book : book.name)
        _logger.info(f'============= sort field{book_list} =======================')

         

        #  Mapped is used to get the values of a specific field from a recordset. 
    def mapped_method(self):
         book = self.env['library.library'].search([])

         book_author = book.mapped('author')
         _logger.info(f'============= map the field{book_author} =======================')



    # def add_record(self):
    #    self.env['school.department'].create({
    #         "department_name": "custom_dp",
    #         "department_description":"custom dp",
    #         "department_head": "head"
    #     })  

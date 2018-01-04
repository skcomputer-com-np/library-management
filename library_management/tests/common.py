# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase

class Common(TransactionCase):
    def setUp(self):
        super(Common,self).setUp() 

         # for student details 
        self.student = self.env['res.partner'].create({

                'name': 'sushil',
                'mobile' : '8511444317',
                'email':"sushil@gmail.com",
                'gender':"male",
                'divisoin': '1'
            })


        # for book details
        self.author = self.env['res.partner'].create({
                'name': 'Vikrant',
                'mobile' : '123456789',
                'email':"vikrant@gmail.com",
                'gender':"male"
            })

        self.publisher = self.env['res.partner'].create({
                'name': 'RS Agrawal',
                'mobile' : '9874563210',
                'email':"rsagrawal@gmail.com",
                'gender':"male"
            })        

        self.material_book = self.env['material'].create({
                'name'  : 'Book'
            })

        self.material_eboook = self.env['material'].create({
                'name'  : 'E-book'
            })

        self.book   =   self.env['product.template'].create({
                'name'              : 'C++',
                'book_type'         : [(6,0,[self.material_book.id,],[self.material_eboook,])],
                'isbn'              : '001',
                'publisher'         : self.publisher.id,
                'author'            : self.author.id,
                'copies'            : 5,
                'standard_price'    : 650.00,
            })


        # for issue book
        self.issue  = self.env['issue.book'].create({
            'stud_id'   :   self.student.id,
            'name'      :   self.book.id,
            'isbn'      :   '001',
            'issue_date':   '01/02/2018',
            'due_date'  :   '01/17/2018',
            })

        # for return book
        self.return_book  = self.env['return.book'].create({
            'stud_name'     :   self.student.id,
            'name'          :   self.book.id,
            'isbn'          :   '001',
            'issue_date'    :   '2018-01-02',
            'due_date'      :   '2018-01-03',
            'return_date'   :   '2018-01-04',
            'fine'          :   0.00,
            'status'        :   True,
            })


















    #     print(age)
    #     print(self.age)
    # def test_00(self):
    #     pass

    # def test_age(self):
    #     self.age =20
    #     age=30
    #     print(self.age)


    # def test_age2(self):
    #     print(self.age)

    # def __init__(self):
    #     self.name = "sushil";
    #     self.age = 22;
    #     self.hobby = "Error solving"

    #     print(self.name)
    #     print(self.age)
    #     print(self.hobby)

    # def setUp(self):
    #     # super(Common,self).setUp()
    #     self.name = "sushil";
    #     self.age = 22;
    #     self.hobby = "Error solving"

    # def test_first(self):

    #     print(self.name)
    #     print(self.age)
    #     print(self.hobby)

    #     self.name = "mishan"
    #     self.age = 24
    #     self.hobby = "playing cricket"

    #     print("test_first called")
    #     print(self.name)
    #     print(self.age)
    #     print(self.hobby)

    # def test_second(self):

    #     print(self.name)
    #     print(self.age)
    #     print(self.hobby) 

    #     self.name = "chirag"
    #     self.age = 23
    #     self.hobby = "playing chess"

    #     print("test_second called.")
    #     print(self.name)
    #     print(self.age)
    #     print(self.hobby)

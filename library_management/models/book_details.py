# -*- coding: utf-8 -*-
import datetime
from odoo import api, fields, models,_
from odoo.exceptions import UserError,ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _sql_constraints = [('Isbn unique','unique(isbn)','Enter unique isbn number...!')]
    role_librarian =fields.Boolean(string="Librarian")
    
    book_type       = fields.Many2many('material', string='Book Type')
    isbn            = fields.Char(string='ISBN')
    Description     = fields.Text(string='Description')
    language        = fields.Many2many('book.language',string='Book Language')
    author          = fields.Many2one('res.partner',domain=[('is_status', "=", "author")])
    publisher       = fields.Many2one('res.partner',domain=[('is_status', "=", "publisher")])
    copies          = fields.Integer(string="Copies",default=0)
    book_avail      = fields.Integer(string="Available",default=0)
    date            = fields.Date(string="Date",default=datetime.datetime.now())
    state           = fields.Selection([
                        ('draft'  , 'Draft' ),
                        ('avail', 'Available' ),
                        ('not_avail', 'Not Available' ),
                        ], default='draft')
# isbn shoud be unique constrains
    @api.constrains('isbn')
    def unique_isbn(self):
        pass

    # @api.constrains('standard_price')
    # def checkBookCost(self):
    #     if self.standard_price == 0:
    #         raise UserError(_("Enter valid price..!"))

    @api.constrains('copies')
    def checkBookCopies(self):
        if self.copies <= 0:
            raise UserError(_("Enter valid available book copies..!"))

    def on_book_avail(self,current_avail):
        print("on book avail called")
        if current_avail == 0:
            self.write({'state':'not_avail'})
        else:
            self.write({'state':'avail'})


    @api.one
    def state_book_avail(self):
        if self.copies:
            self.write({'state':'avail'})
            self.write({'book_avail':self.copies})
        else:
            raise UserError(_("Fill book copies field...!"))
    
class Materials(models.Model):
    _name ="material"
    name = fields.Char("Book Type")

class BookLanguage(models.Model):
    _name = "book.language"
    name  = fields.Char()



class ProductAttributeLine(models.Model):
    _inherit = "product.attribute.line"

    qty = fields.Integer(string='Quantity')             
    

    # ./odoo-bin -d asd --db-filter=asd --addons-path=addons,../library-management -u library_management
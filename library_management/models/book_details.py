# -*- coding: utf-8 -*-
import datetime
from odoo import api, fields, models,_
from odoo.exceptions import UserError,ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _sql_constraints = [('Isbn unique','unique(isbn)','Enter unique isbn number...!')]
    role_librarian =fields.Boolean(string="Librarian")
    
    book_type = fields.Many2many('material', string='Book Type')
    isbn = fields.Char(string='ISBN')
    Description = fields.Text(string='Description')
    language = fields.Many2many('book.language',string='Book Language')
    author = fields.Many2one('res.partner',domain=[('is_status', "=", "author")])
    publisher = fields.Many2one('res.partner',domain=[('is_status', "=", "publisher")])
    copies = fields.Integer(string="Copies",default=0)
    temp_copies = fields.Integer(default=0)
    book_avail = fields.Integer(string="Available",default=0)
    date = fields.Date(string="Date",default=datetime.datetime.now())
    state = fields.Selection([
                        ('draft'  , 'Draft' ),
                        ('avail', 'Available' ),
                        ('not_avail', 'Not Available' ),
                        ], default='draft')
# isbn shoud be unique constrains
    @api.constrains('isbn')
    def unique_isbn(self):
        pass

    def on_book_avail(self,current_avail):
        print("on book avail called")
        if self.state != "draft":
            if current_avail == 0:
                self.write({'state': 'not_avail'})
            else:
                self.write({'state': 'avail'})

    @api.one
    def state_book_avail(self):
        if self.copies:
            self.write({'state':'avail'})
            self.write({'book_avail':self.copies})
            obj = self.env['product.template'].search([('isbn','=',self.isbn)])
            obj.write({'temp_copies':self.copies})
        else:
            raise UserError(_("Fill book copies field...!"))

    @api.onchange('copies')
    def addValueToTempCopies(self):
        if self.state == "avail":            
            obj = self.env['product.template'].search([('isbn','=',self.isbn)])
            if obj.state == "avail":
                old_available = obj.book_avail
                old_copies = obj.temp_copies
                new_copies = self.copies
                temp_book_avail = new_copies - (old_copies - old_available)       
                obj.write({'book_avail':temp_book_avail})               
                obj.write({'temp_copies':new_copies})
                if temp_book_avail != 0:
                    obj.write({'state': 'avail'})
                else:
                    obj.write({'state': 'not_avail'})
                    obj.write({'book_avail': 0})

        if self.state == 'not_avail':
            obj = self.env['product.template'].search([('isbn', '=', self.isbn)])
            old_copies = obj.temp_copies
            new_copies = self.copies
            temp_book_avail = new_copies - old_copies       
            obj.write({'book_avail': temp_book_avail})
            obj.write({'temp_copies': new_copies})
            obj.write({'state': 'avail'})
    
class Materials(models.Model):
    _name ="material"
    name = fields.Char("Book Type")

class BookLanguage(models.Model):
    _name = "book.language"
    name  = fields.Char()

class ProductAttributeLine(models.Model):
    _inherit = "product.attribute.line"

    qty = fields.Integer(string='Quantity')
# -*- coding: utf-8 -*-
import datetime
from odoo import api, fields, models,_
from odoo.exceptions import UserError,ValidationError

class ProductTemplate(models.Model):
	_inherit = 'product.template'
	_sql_constraints = [('Isbn unique','unique(isbn)','Enter unique isbn number...!')]
	role_librarian =fields.Boolean(string="Librarian")
	
	book_type 		= fields.Many2many('material', string='Book Type')
	isbn 			= fields.Char(string='ISBN')
	Description 	= fields.Text(string='Description')
	language 		= fields.Many2many('book.language',string='Book Language')
	author 			= fields.Many2one('res.partner',domain=[('is_status', "=", "author")])
	publisher 		= fields.Many2one('res.partner',domain=[('is_status', "=", "publisher")])
	copies 			= fields.Integer(string="Copies",default=0)
	book_avail 		= fields.Integer(string="Available",default=0)
	date 			= fields.Date(string="Date",default=datetime.datetime.now())
	state			= fields.Selection([
						('req'	, '	Request' ),
						('avail', 'Available' ),
						('not_avail', 'Not Available' ),
		])
	req_book 		= fields.Boolean('Request book')
	qty 			= fields.Integer(string='Quantity') 			
	
	# student

	stud_ids = fields.Many2one('res.partner',domain=[('is_status', "=", "stud")])	
	rno = fields.Char(string="Roll No")
	division = fields.Selection(
		[
			('1','A'),
			('2','B'),
			('0','Other'),
		],string='Division')



# isbn shoud be unique constrains
	@api.constrains('isbn')
	def unique_isbn(self):
		pass

# request book state
	@api.one
	def state_book_request(self):
		self.write({'state':'req'})

# book available changed
	@api.onchange('book_avail','copies')
	def on_book_avail(self):
		if self.book_avail  == 0 or self.copies  == 0 :
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
	
	# @api.model
	# def create(self,vals):		
	# 	obj=super(ProductTemplate,self).create(vals)
	# 	result = self.env['product.template'].search([('name', '=', obj.name)])
	# 	print("stud_ids ===============>> ",result.stud_ids)
	# 	print("req_book ===============>> ",result.req_book)
	# 	return obj

class Materials(models.Model):
	_name ="material"
	name = fields.Char("Book Type")

class BookLanguage(models.Model):
	_name = "book.language"
	name  = fields.Char()










	# ./odoo-bin -d asd --db-filter=asd --addons-path=addons,../library-management -u library_management

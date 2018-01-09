# -*- coding: utf-8 -*-

from odoo import api, fields, models,_
from odoo.exceptions import UserError,ValidationError
from datetime import datetime,date
import datetime
class IssueBook(models.Model):

	_name = "issue.book"
	_description = "Issue Book Details"

	stud_id = fields.Many2one('res.partner','Student', domain=[('is_status', "=", "stud")])
	name = fields.Many2one('product.template', 'Book',domain=[('role_librarian', '=', True)])
	isbn = fields.Char('ISBN')
	issue_date = fields.Date(string='Issued Date',default=datetime.datetime.now())
	due_date = fields.Date(string='Due Date')
	state = fields.Selection([			
			('draft','Draft'),
			('book_issue','Issued'),
			('fine_cal','Fine Calculated'),
			('book_return','Returned'),
		],default='draft')

	# for return
	return_date 	= fields.Date(string='Return Date',default=datetime.datetime.now())
	fine_resion	= fields.Many2one('make.fine.resion')
	fine 			= fields.Float(string='Total Fine')


	@api.constrains('isbn')
	def check_isbn(self):
		if not self.isbn:
			raise ValidationError(_('Invalid isbn number...!'))	
			
	@api.one
	def state_book_issue(self):
		obj = self.env['product.template'].search([('isbn','=',self.isbn)])
		issue_date1 =  self.issue_date
		due_date1 	=  self.due_date		

		issue_date = issue_date1.split('-')
		due_date   = due_date1.split('-')

		diff = date(int(due_date[0]),int(due_date[1]),int(due_date[2]))-date(int(issue_date[0]),int(issue_date[1]),int(issue_date[2]))

		if diff.days < 0:
			raise UserError(_("Due date should be greater than issue date..!"))
		
		if obj:			
			if obj.state == 'avail':
				obj.write({'book_avail':obj.book_avail - 1})
				self.write({'state': 'book_issue'})
				obj.on_book_avail(obj.book_avail)

			else:
				raise UserError(_("Book is not availble...!"))
		else:
			raise UserError(_("No book found having...!"))

	@api.one
	def state_book_return(self):			
		self.checkFine()
		obj = self.env['product.template'].search([('isbn','=',self.isbn)])
		obj.write({'book_avail':obj.book_avail + 1})
		obj.on_book_avail(obj.book_avail)
		self.write({'state': 'book_return'})
		
	@api.one
	def checkFine(self):
		self.write({'state': 'fine_cal'})		
		

	@api.onchange('fine_resion')
	def fineCalculated(self):
		if self.state == 'fine_cal' :
			obj = self.env['product.template'].search([('isbn','=',self.isbn)])		
			if obj :
				return_date1 =  self.return_date
				due_date1  	 =  self.due_date
				return_date = return_date1.split('-')
				due_date    = due_date1.split('-')
				diff = date(int(due_date[0]),int(due_date[1]),int(due_date[2]))-date(int(return_date[0]),int(return_date[1]),int(return_date[2]))		
				if diff.days < 0:	
					if self.fine_resion.per == True:
						self.fine = (obj.standard_price * float(self.fine_resion.value)/100)
					else:
						self.fine = abs(diff.days)* self.fine_resion.value
				else:
					self.fine = 00.0;
			else:
				raise UserError("There is no any book having isbn ",self.isbn)


class MakeFineResion(models.Model):
	_name = "make.fine.resion"

	name 	= fields.Char(name="Resion")
	value 	= fields.Char(name="Value")
	per 	= fields.Boolean(string="Per(%)",default=False)

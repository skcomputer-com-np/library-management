# -*- coding: utf-8 -*-

from odoo import api, fields, models,_
from odoo.exceptions import UserError,ValidationError
import datetime
class IssueBook(models.Model):

	_name = "issue.book"
	_description = "Issue Book Details"

	stud_id = fields.Many2one('res.partner','Student Name', domain=[('is_status', "=", "stud")])
	name = fields.Many2one('product.template', 'Book Name',domain=[('role_librarian', '=', True)])
	isbn = fields.Char('ISBN')
	issue_date = fields.Date(string='Issued Date',default=datetime.datetime.now())
	due_date = fields.Date(string='Due Date')
	state = fields.Selection([
			('book_not_avail','Not available'),
			('book_avaii','Available'),
			('book_issue','Issue'),
			('book_return','Return'),
		])

	@api.constrains('isbn')
	def check_isbn(self):
		if not self.isbn:
			raise ValidationError(_('Invalid isbn number...!'))
	# @api.onchange('isbn')
	# def onchange_isbn(self):
	# 	obj = self.env['product.template'].search([('id', '=', self.name.id),('isbn', '=', self.isbn)])
	# 	self.env['issue.book'].write({
	#         'state': 'book_avaii',
	#     })
			
	@api.one
	def state_book_issue(self):
		obj = self.env['product.template'].search([('isbn','=',self.isbn)])
		if obj:
			print("+================>"+obj.state)
			if obj.state == 'avail':
				obj.write({'book_avail':obj.book_avail - 1})
				self.write({'state': 'book_issue'})
			else:
				raise UserError(_("Book is not availble having isbn ",self.isbn))
		else:
			raise UserError(_("No book found having isbn ",self.isbn))
	@api.one
	def state_book_return(self):
	    self.write({
	        'state': 'book_return',
	    })

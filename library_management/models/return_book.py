# -*- coding: utf-8 -*-

from odoo import api, fields, models,_
from odoo.exceptions import UserError,ValidationError
from datetime import datetime,date
import math

class ReturnBook(models.Model):
	_name = "return.book"
	_description = "Return Book Details"

	stud_name 		= fields.Many2one('res.partner', domain=[('is_status', '=', "stud")])
	name 			= fields.Many2one('product.template',domain=[('role_librarian', '=', True)])
	isbn	 		= fields.Char(string='ISBN')
	issue_date 		= fields.Char(string='Issue Date')
	due_date 		= fields.Char(string='Due Date')
	return_date 	= fields.Char(string='Return Date',default=datetime.now().date())
	fine_per_day 	= fields.Float(string='Fine Per Day')
	fine 			= fields.Float(string='Total Fine')
	status 			= fields.Boolean(string="Is return")

	# name_ids 	= fields.Many2one('fine.resion')

	@api.onchange('isbn')
	def onchange_set_value(self):
		try:
			if self.stud_name and self.name and self.isbn:
				obj = self.env['issue.book'].search([('stud_id', '=', self.stud_name.id),('isbn', '=', self.isbn)])
				print (obj)
				self.issue_date = obj.issue_date
				self.due_date = obj.due_date
			else:
				self.issue_date ="" 
				self.due_date =""
				
		except Exception as e:
			pass

	@api.constrains('stud_name')
	def check_isbn(self):		
		if not self.stud_name:
			raise ValidationError(_('Invalid student name...!'))

	@api.constrains('isbn')
	def check_isbn(self):		
		if not self.isbn:
			raise ValidationError(_('Invalid isbn number...!'))


	@api.constrains('due_date')
	def check_issue_date(self):		
		if not self.issue_date:
			raise ValidationError(_('Invalid issue date...!'))
	

	@api.constrains('return_date')
	def check_return_date(self):		
		if not self.return_date:
			raise ValidationError(_('Invalid return date...!'))

	@api.model
	def create(self,vals):
		date1=vals['due_date']
		date2=vals['return_date']
		lst=date1.split("-")
		lst1=date2.split("-")
		diff=date(int(lst[0]),int(lst[1]),int(lst[2]))-date(int(lst1[0]),int(lst1[1]),int(lst1[2]))
		if diff.days<0:
			vals['fine']=abs(diff.days*1)

		obj=super(ReturnBook,self).create(vals)


		# result = self.env['issue.book'].search([('stud_id', '=', obj.stud_name.id), ('name', '=', obj.name.id),('isbn','=',obj.isbn)])
		# if result:
		# 	result.unlink()

		#raise Warning(_("You Would require to pay {}".format(vals['fine'])))
		return obj
	

# class FineResion(models.Model):
# 	_name = "fine.resion"

# 	name = fields.Selection([			
# 			('regular','Regular'),
# 			('damage','Damaged'),
# 			('lost','Lost'),
# 		],default='regular')

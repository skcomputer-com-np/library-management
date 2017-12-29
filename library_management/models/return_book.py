# -*- coding: utf-8 -*-

from odoo import api, fields, models,_
from odoo.exceptions import Warning
from datetime import datetime,date
import math

class ReturnBook(models.Model):
	_name = "return.book"
	_description = "Return Book Details"

	stud_name 		= fields.Many2one('res.partner', domain=[('is_status', '=', "stud")])
	name 			= fields.Many2one('product.template',domain=[('book_type', '=', "Book")])
	issue_date 		= fields.Char(string='Issue Date')
	due_date 		= fields.Char(string='Due Date')
	return_date 	= fields.Char(string='Return Date',default=datetime.now().date())
	fine 			= fields.Float(string='Fine')
	status 			= fields.Boolean(string="Is return")

	# domain=[('is_status', '=', "stud")]
	# ./odoo-bin -d asd --db-filter=asd --addons-path=addons,../library-management -u library_management

	@api.onchange('name')
	def onchange_set_value(self):
		try:
			if self.stud_name and self.name:
				obj = self.env['issue.book'].search([('stud_id', '=', self.stud_name.id), ('name', '=', self.name.id)])
				print (obj)
				self.issue_date = obj.issue_date
				self.due_date = obj.due_date
				
		except Exception as e:
			pass
	@api.model
	def create(self,vals):
		date1=vals['due_date']
		date2=vals['return_date']
		print(date1)
		print(date2)
	
		lst=date1.split("-")
		lst1=date2.split("-")
		diff=date(int(lst[0]),int(lst[1]),int(lst[2]))-date(int(lst1[0]),int(lst1[1]),int(lst1[2]))
		if diff.days<0:
			vals['fine']=abs(diff.days*1)

		obj=super(ReturnBook,self).create(vals)

		result = self.env['issue.book'].search([('stud_id', '=', obj.stud_name.id), ('name', '=', obj.name.id)])
		if result:
			result.unlink()

		#raise Warning(_("You Would require to pay {}".format(vals['fine'])))
		return obj

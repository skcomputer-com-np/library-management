# -*- coding: utf-8 -*-

from odoo import api, fields, models
import datetime
class IssueBook(models.Model):
	_name = "issue.book"
	_description = "Issue Book Details"

	stud_id = fields.Many2one('res.partner',string='Student Name', domain=[('is_status', '=', "stud")])
	name = fields.Many2one('product.template', 'Book Name',domain=[('book_type', '=', "Book")])
	issue_date = fields.Date(string='Issued Date',default=datetime.datetime.now())
	due_date = fields.Date(string='Return Date')
	# status = fields.Selection(
	# 	[
	# 		('1','Issued'),
	# 		('2','Returned'),
	# 		('0','Other')
	# 	])

	# ./odoo-bin -d asd --db-filter=asd --addons-path=addons,../library-management -u library_management

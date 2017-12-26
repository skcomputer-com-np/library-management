# -*- coding: utf-8 -*-

from odoo import api, fields, models

class IssueBook(models.Model):
	_name = "issue.book"
	_description = "Issue Book Details"

	issue_id = fields.Char(string='Issue Book Id: ')
	stud_id = fields.Char(string='Student Id: ',required=True)
	issue_book_title = fields.Text(string='Issue Book Title: ', required=True)
	issue_date = fields.Date(string='Issued Date: ')
	return_date = fields.Date(string='Return Date: ')
	fine = fields.Float(string='Fine : ')
	status = fields.Selection(
		[
			('1','Issued'),
			('2','Returned'),
			('0','Other')
		])

	# ./odoo-bin -d asd --db-filter=asd --addons-path=addons,../library-management -u library_management

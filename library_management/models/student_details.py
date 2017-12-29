# -*- coding: utf-8 -*-

from odoo import api, fields, models

class StudentDetails(models.Model):
	_inherit = 'res.partner'

	is_status = fields.Selection(
		[
			('stud','Student'),
			('faculty','Faculty'),
			('admin','Admin'),
		],

		default='stud'

		)

	gender = fields.Selection(
		[
			('male','Male'),
			('female','Female'),
			('other','Other')
		])
	divisoin = fields.Selection(
		[
			('1','A'),
			('2','B'),
			('0','Other')
		])
	date = fields.Date("Date")

	@api.onchange('is_status')
	def onchange_standard(self):
		if self.is_status  == 'stud' :
			 self.function  = 'Student'

		elif self.is_status == 'faculty':
			 self.function 	= 	'Faculty'

		elif self.is_status == 'admin':
			 self.function 	= 	'Admin'

	# ./odoo-bin -d asd --db-filter=asd --addons-path=addons,../library-management -u library_management

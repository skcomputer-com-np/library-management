# -*- coding: utf-8 -*-

from odoo import api, fields, models

class StudentDetails(models.Model):
	_name = "student.details"
	_description = "Student Details"

	stud_id = fields.Char(string='Student Id: ',required=True)
	stud_name = fields.Char(string='Student Name: ',required=True)
	gender = fields.Selection(
		[
			('male','Male'),
			('female','Female'),

		])

	mobile_no = fields.Char('Mobile No: ')
	address = fields.Text('Address: ')
	city = fields.Char('City: ')
	pin_code = fields.Integer('Pin Code: ')
	email = fields.Char('Email Id: ')
	divisoin = fields.Selection(
		[
			('1','A'),
			('2','B'),
			('0','Other')
		])
	date = fields.Date("Date: ")



	# ./odoo-bin -d asd --db-filter=asd --addons-path=addons,../library-management -u library_management

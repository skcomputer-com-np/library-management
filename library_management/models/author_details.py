# -*- coding: utf-8 -*-

from odoo import api, fields, models

class AuthorDetails(models.Model):
	_name = "author.details"
	_description = "Author Details"

	name = fields.Char(string='Author Name')
	# code = fields.Integer(string='Code')

	
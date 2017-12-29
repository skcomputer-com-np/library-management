# -*- coding: utf-8 -*-

from odoo import api, fields, models

class CategoryDetails(models.Model):
	_name = "category.details"
	_description = "Category Details"

	name = fields.Char(string='Book Category Name')
	# code = fields.Integer(string='Code')

	
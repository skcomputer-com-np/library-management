# -*- coding: utf-8 -*-

from odoo import api, fields, models

class AuthorDetails(models.Model):
	_name = "publisher.details"
	_description = "Publisher Details"

	name = fields.Char(string='Publisher Name')

	
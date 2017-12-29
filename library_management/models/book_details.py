# -*- coding: utf-8 -*-

from odoo import api, fields, models

class BookDetails(models.Model):
	_inherit = 'product.template'
	role_librarian =fields.Boolean(string="Librarian")
	
	book_type = fields.Many2many('material', string='Book Type')
	isbn = fields.Integer(string='ISBN')
	description = fields.Text(string='Description')

	language = fields.Selection(
		[
			('english', 'English'), 
			('hindi', 'Hindi'),
			('urdu', 'Urdu'),
			('gujarati', 'Gujarati'),
			('other', 'Other'),
		])
	author = fields.Many2one('author.details',string='Author Name')
	publisher =  fields.Many2one('publisher.details',string='Publisher Name')
	copies = fields.Integer(string="Copies")
	date = fields.Date(string="Date")


class Materials(models.Model):
	_name="material"
	name= fields.Char("Book Type")









	# ./odoo-bin -d asd --db-filter=asd --addons-path=addons,../library-management -u library_management

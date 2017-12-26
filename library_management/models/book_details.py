# -*- coding: utf-8 -*-

from odoo import api, fields, models

class BookDetails(models.Model):
	_name = "book.details"
	_description = "Book Details"

	book_id = fields.Char(string='Book Id: ')
	isbn = fields.Integer(string='ISBN: ')
	title = fields.Char(string='Book Title: ', required=True)
	description = fields.Text(string='Description: ')
	language = fields.Selection(
		[
			('english', 'English'), 
			('hindi', 'Hindi'),
			('urdu', 'urdu'),
			('gujarati', 'Gujarati'),
			('other', 'Other'),
		])
	category = fields.Selection(
		[
			('novel','Novel'),
			('comic','Comic'),
			('drama','Drama'),
			('ebook','E-Book'),
			('magzin','Magzin'),
			('technical','Technical'),
			('management','Management'),
			('social','Social'),
			('other','Other')

		])
	author = fields.Selection(
		[
			('author1','Author1'),
			('author2','Author2'),
			('author3','Author3'),
			('author4','Author4'),
			('author5','Author4'),
			('author6','Author6'),
			('other','Other')

		])
	publisher = fields.Selection(
		[
			('publisher1','Publisher1'),
			('publisher2','Publisher2'),
			('publisher3','Publisher3'),
			('publisher4','Publisher4'),
			('publisher5','Publisher5'),
			('publisher6','Publisher6'),
			('publisher7','Publisher7'),
			('other','Other')
		])
	price = fields.Float(string="Price: ")
	copies = fields.Integer(string="Copies: ")
	# cover_image = fields.
	date = fields.Date(string="Date")













	# ./odoo-bin -d asd --db-filter=asd --addons-path=addons,../library-management -u library_management

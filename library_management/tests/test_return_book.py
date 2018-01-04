# -*- coding: utf-8 -*-
from . import common

class TestReturnBook(common.Common):
	def test_return_book(self):

		self.return_book.stud_name	=	self.student.id
		self.return_book.name		=	self.book.id
		self.return_book.isbn		=	"001"
		
		self.return_book.onchange_set_value()

		print(self.return_book['stud_name'])
		print(self.return_book['name'])
		print(self.return_book.isbn)
		print(self.return_book.issue_date)
		print(self.return_book.due_date)
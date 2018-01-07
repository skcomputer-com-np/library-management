# -*- coding: utf-8 -*-
from . import common

class TestStudentDetails(common.Common):
	def test_is_status(self):
		self.student.onchange_standard()

	# def test_check_phone(self):
	# 	self.student.check_phone_no()

	# def test_check_email(self):
	# 	self.student.check_email()
		

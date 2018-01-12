# -*- coding: utf-8 -*-
from . import common

class TestStudentDetails(common.Common):
	def test_is_status(self):
		self.student.onchange_standard()
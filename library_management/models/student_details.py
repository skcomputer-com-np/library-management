# -*- coding: utf-8 -*-
import datetime
import re
from odoo import api, fields, models,_
from odoo.exceptions import UserError,ValidationError

class StudentDetails(models.Model):
	_inherit= 'res.partner'


	is_status= fields.Selection(
		[
			('stud','Student'),
			('librarian','Librarian'),
			('author','Author'),
			('publisher','Publisher'),
		])

	gender= fields.Selection(
		[
			('male','Male'),
			('female','Female'),
			('other','Other')
		])
	division_ids= fields.Many2one('student.division')

	course_ids= fields.Many2one("student.course")
	date= fields.Date("Date",default=datetime.datetime.now())
	rno= fields.Char(string="Roll No")

	@api.onchange('is_status')
	def onchange_standard(self):
		if self.is_status  == 'stud' :
			 self.function  = 'Student'

		elif self.is_status == 'librarian':
			 self.function 	= 	'Librarian'
		else:
			self.function 	= 	''

	@api.model
	def create(self,vals):
		obj = super(StudentDetails,self).create(vals)
		template = self.env.ref('library_management.registration',raise_if_not_found=False) #note here registration is template id of registration_template.xml
		template.send_mail(obj.id)
		return obj

class StudentCourse(models.Model):
	_name=	'student.course'
	_description=	 "Name of courses"
	_rec_name= "course"

	course= fields.Char(string="Course")

class StudentDivision(models.Model):
	_name= 'student.division'
	_description= "Divisions of student"
	_rec_name= "name"

	name= fields.Char(string="Division")
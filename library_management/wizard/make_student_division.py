# -*- coding: utf-8 -*-

from odoo import models, api, fields


class MakeStudentDivision(models.TransientModel):
    _name = 'make.student.division'
    _description = 'Wizard for Student'

    is_division = fields.Boolean(string="Division")
    is_course = fields.Boolean(string="Course")
    division_ids = fields.Many2one("student.division")
    course_ids = fields.Many2one("student.course")
    
    @api.multi
    def change_division(self):
        active_ids = self.env.context['active_ids']        
        lines = self.env['res.partner'].search([('id', 'in', active_ids)])
        for line in lines:         
            if self.is_division:                
                line.write({'division_ids': self.division_ids.id})
            
            if self.is_course:                
                line.write({'course_ids': self.course_ids.id})

            if self.is_division and self.is_course:
                line.write({
                    'course_ids' : self.course_ids.id,
                    'division_ids'   : self.division_ids.id,
                    })


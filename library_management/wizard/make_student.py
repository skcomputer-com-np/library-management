# -*- coding: utf-8 -*-

from odoo import models, api, fields


class Student(models.TransientModel):
    _name = 'make.student'
    _description = 'Wizard for Student'

    age = fields.Integer("Age")

    @api.multi
    def state_student(self):
        active_ids = self.env.context['active_ids']
        lines = self.env['res.partner'].search([('id', 'in', active_ids)])
        for line in lines:
            line.write({'is_student': True})

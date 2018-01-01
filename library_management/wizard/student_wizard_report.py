# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import time
from odoo import api, fields, models, _
from odoo.exceptions import UserError
class StudentDetailsSummary(models.TransientModel):

    _name = 'student.details.summary'

    date_from = fields.Date(string='From', required=True, default=lambda *a: time.strftime('%Y-%m-01'))
    date_to = fields.Date(string='To', required=True,
                            default=lambda *a: time.strftime('%Y-%m-31'))

    @api.multi
    def print_report(self):
        self.ensure_one()
        [data] = self.read()
        students = self.env['res.partner'].search([('date','>=',data['date_from'])])
        # print("======================>",students)
        # print('\n\n\n')
        # students = self.env['res.partner'].browse()
        # datas = {
        #     'ids': [],
        #     'model': 'res.partner',
        #     'form': data
        # }
        return self.env.ref('library_management.wizard_action_report_student_detail').report_action(students)

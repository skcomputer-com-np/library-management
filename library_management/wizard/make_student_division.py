# -*- coding: utf-8 -*-

from odoo import models, api, fields


class MakeStudentDivision(models.TransientModel):
    _name = 'make.student.division'
    _description = 'Wizard for Student'

    
    @api.multi
    def change_division(self):

        # print("\n\n\nSELF :::::: ",self)
        # print("\n\n\nAge :::::: ",self.age)
        #
        # print("\n\n\n self.env.context ::: ", self.env.context)
        # print("\n\n\n self.env.context ::: ", self._context)    
        # print("\n\n\n self.env.context ::: ", self.env.context['my_msg'])
        active_ids = self.env.context['active_ids']        
        lines = self.env['res.partner'].search([('id', 'in', active_ids)])
        for line in lines:            
            line.write({'divisoin': '1'})
        

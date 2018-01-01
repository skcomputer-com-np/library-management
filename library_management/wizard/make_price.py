# -*- coding: utf-8 -*-

from odoo import models, api, fields


class MakePrice(models.TransientModel):
    _name = 'make.price'
    _description = 'Wizard for book brice '

    book_price = fields.Float("Price")

    @api.multi
    def change_price(self):

        # print("\n\n\nSELF :::::: ",self)
        # print("\n\n\nAge :::::: ",self.age)
        #
        # print("\n\n\n self.env.context ::: ", self.env.context)
        # print("\n\n\n self.env.context ::: ", self._context)    
        active_ids = self.env.context['active_ids']        
        lines = self.env['product.template'].search([('id', 'in', active_ids)])
        for line in lines:            
            line.write({'standard_price': self.book_price})       

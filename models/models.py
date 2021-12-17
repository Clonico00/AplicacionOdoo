# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odoo168(models.Model):
#     _name = 'odoo168.odoo168'
#     _description = 'odoo168.odoo168'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api

class manga(models.Model):
	_name = 'odoo168.manga'
	_description = 'model manga'

	name = fields.Char('Id',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	autor = fields.Char(string='Autor',required=True)

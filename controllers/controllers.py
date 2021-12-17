# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo168(http.Controller):
#     @http.route('/odoo168/odoo168/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo168/odoo168/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo168.listing', {
#             'root': '/odoo168/odoo168',
#             'objects': http.request.env['odoo168.odoo168'].search([]),
#         })

#     @http.route('/odoo168/odoo168/objects/<model("odoo168.odoo168"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo168.object', {
#             'object': obj
#         })

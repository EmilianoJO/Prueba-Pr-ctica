# -*- coding: utf-8 -*-
# from odoo import http


# class Assesment1(http.Controller):
#     @http.route('/assesment1/assesment1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/assesment1/assesment1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('assesment1.listing', {
#             'root': '/assesment1/assesment1',
#             'objects': http.request.env['assesment1.assesment1'].search([]),
#         })

#     @http.route('/assesment1/assesment1/objects/<model("assesment1.assesment1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('assesment1.object', {
#             'object': obj
#         })

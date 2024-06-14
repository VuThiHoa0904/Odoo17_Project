# -*- coding: utf-8 -*-
# from odoo import http


# class LogisticCustom(http.Controller):
#     @http.route('/logistic_custom/logistic_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/logistic_custom/logistic_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('logistic_custom.listing', {
#             'root': '/logistic_custom/logistic_custom',
#             'objects': http.request.env['logistic_custom.logistic_custom'].search([]),
#         })

#     @http.route('/logistic_custom/logistic_custom/objects/<model("logistic_custom.logistic_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('logistic_custom.object', {
#             'object': obj
#         })


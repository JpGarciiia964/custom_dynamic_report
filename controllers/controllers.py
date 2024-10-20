# -*- coding: utf-8 -*-
# from odoo import http


# class CustomDynamicReport(http.Controller):
#     @http.route('/custom_dynamic_report/custom_dynamic_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_dynamic_report/custom_dynamic_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_dynamic_report.listing', {
#             'root': '/custom_dynamic_report/custom_dynamic_report',
#             'objects': http.request.env['custom_dynamic_report.custom_dynamic_report'].search([]),
#         })

#     @http.route('/custom_dynamic_report/custom_dynamic_report/objects/<model("custom_dynamic_report.custom_dynamic_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_dynamic_report.object', {
#             'object': obj
#         })

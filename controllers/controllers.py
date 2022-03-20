# -*- coding: utf-8 -*-
from odoo import http


class OdooVeterinary(http.Controller):
     @http.route('/odoo_veterinary/odoo_veterinary/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/odoo_veterinary/odoo_veterinary/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('odoo_veterinary.listing', {
             'root': '/odoo_veterinary/odoo_veterinary',
             'objects': http.request.env['odoo_veterinary.odoo_veterinary'].search([]),
         })

     @http.route('/odoo_veterinary/odoo_veterinary/objects/<model("odoo_veterinary.odoo_veterinary"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('odoo_veterinary.object', {
             'object': obj
         })

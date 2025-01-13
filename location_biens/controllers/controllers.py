# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
import json
from odoo import http, SUPERUSER_ID

from odoo.addons.payment.controllers.portal import PaymentProcessing



    
class WebsiteSaleInherit(WebsiteSale):    

   

    def _get_search_domain(self, search, category, attrib_values):
        domain = request.website.sale_product_domain()
        if search:
            for srch in search.split(" "):
                domain += [
                    '|', '|', '|', '|', '|', '|', ('name', 'ilike', srch), ('nom_ville_site', 'ilike', srch),
                    ('default_code', 'ilike', srch), ('name_quartier_site', 'ilike', srch),
                    ('description_sale', 'ilike', srch), ('product_variant_ids.default_code', 'ilike', srch), ('name_pays_site', 'ilike', srch)]
                    
        if category:
            domain += [('public_categ_ids', 'child_of', int(category))]

        if attrib_values:
            attrib = None
            ids = []
            for value in attrib_values:
                if not attrib:
                    attrib = value[0]
                    ids.append(value[1])
                elif value[0] == attrib:
                    ids.append(value[1])
                else:
                    domain += [('attribute_line_ids.value_ids', 'in', ids)]
                    attrib = value[0]
                    ids = [value[1]]
            if attrib:
                domain += [('attribute_line_ids.value_ids', 'in', ids)]

        return domain


class Hospital(http.Controller):    
    
    
    
    
    
    
 
    
    @http.route('/hello/boutique', website=True, auth='user')
    def hello(self, **kw):
        product_variant = request.env['product.product'].browse('product_id')
        return request.render("location_biens.location_thanks")
        
        
        
  
    @http.route('/patient_webform', type="http", auth="public", website=True)
    def patient_webform(self, **kw):
        print("Execution Here.........................")
       # doctor_rec = request.env['product.product'].sudo().search([])
        #print("doctor_rec...", doctor_rec)
        return http.request.render('location_biens.create_patient', {'name': 'Odoo Mates Test 123'})

    @http.route('/create_location/boutique', type="http", auth="public", website=True)
    def create_webpatient(self, **kw):
        print("Data Received.....", kw)
        request.env['crm.lead'].sudo().create(kw)
        # doctor_val = {
        #     'name': kw.get('patient_name')
        # }
        # request.env['hospital.doctor'].sudo().create(doctor_val)
        return request.render("location_biens.location_thanks")    
        





class Main(http.Controller):
    @http.route('/todo', website=True, auth='user')
    def index(self, **kw):
        products = request.env['product.product'].sudo().search([('name_adresse_t', "ilike", self)], order="chambres asc")
        return request.render("location_biens.index", {'product': products})

       
class Main_detail(http.Controller):
    @http.route('/todo/<model("product.product"):task>', website=True)
    def index(self, task, **kw):
        return http.request.render('location_biens.detail',{'product': task})




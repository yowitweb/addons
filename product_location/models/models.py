# -*- coding: utf-8 -*-
import werkzeug
from odoo import models, fields, api

def urlplus(url, params):
    return werkzeug.Href(url)(params or None)

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    location = fields.Many2one('product.location', string='Adresse', ondelete='restrict', required=True)
                               #, domain="[('user_id', '=', uid)]") # create_uid
    
    @api.multi
    def google_map_img(self, zoom=8, width=600, height=100):
        self.ensure_one()
        if self.location:
            return self.sudo().location.google_map_img(zoom=zoom, width=width, height=height)
        return None

    @api.multi
    def google_map_link(self, zoom=8):
        self.ensure_one()
        if self.location:
            return self.sudo().location.google_map_link(zoom=zoom)
        return None
    
class Users(models.Model):
    _inherit = "res.users"
    
    locations = fields.One2many('product.location', 'user_id')
                                #, default=lambda self: self.env.user.company_id.partner_id)


class ProductLocation(models.Model):
    _name = 'product.location'
    _description = 'Product Location'
    
    user_id = fields.Many2one("res.users")
    product_ids = fields.One2many("product.template", 'location')
    name = fields.Char(required=True, index=True, string='Rue')
    name2 = fields.Char(string='Quartier')
    zip = fields.Char(change_default=True, string='BP')
    city = fields.Char(required=True, index=True, string='City')
    state_id = fields.Many2one(
        "res.country.state", string='State', 
        ondelete='restrict', index=True, required=True)
    country_id = fields.Many2one(
        'res.country', string='Country',
        related='state_id.country_id',
        ondelete='restrict', index=True, required=True)
    phone = fields.Char(string='Phone')

    @api.multi
    def google_map_img(self, zoom=8, width=600, height=100):
        google_maps_api_key = self.env['ir.config_parameter'].sudo().get_param('google_maps_api_key')
        if not google_maps_api_key:
            return False
        params = {
            'center': '%s, %s %s, %s' % (self.name or '', self.city or '', self.zip or '', 
                                         self.country_id and self.country_id.name_get()[0][1] or ''),
            'size': "%sx%s" % (width, height),
            'zoom': zoom,
            'key': google_maps_api_key,
        }
        return urlplus('//maps.googleapis.com/maps/api/staticmap', params)

    @api.multi
    def google_map_link(self, zoom=10):
        params = {
            'q': '%s, %s %s, %s' % (self.name or '', self.city or '', self.zip or '', 
                                    self.country_id and self.country_id.name_get()[0][1] or ''),
            'z': zoom,
        }
        return urlplus('https://maps.google.com/maps', params)

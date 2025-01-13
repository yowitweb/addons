# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name" : "Website Gift Wrap/Packing Odoo",
    "version" : "12.0.1.3",
    "category" : "eCommerce",
    "depends" : ['website','website_sale','sale_management'],
    "author": "BrowseInfo",
    "summary": 'This module helps to Add Gift Wrap for product on Odoo eCommerce',
    "description": """
        Website Gift Wrap
        Website Gift pack
        Gift Wrap on website
        Gift pack on website
        Gift package on website
        
        webshop Gift Wrap
        webshop Gift pack
        Gift Wrap on webshop
        Gift pack on webshop
        Gift package on webshop
        
        
        shop Gift Wrap
        shop Gift pack
        website Gift Wrap on shop
        website Gift pack on shop
        website Gift package on shop
        website gift packing website
        website gift card website
       
        
    """,
    "website" : "www.browseinfo.in",
    "data": [
        'security/ir.model.access.csv',
        'views/giftwrap.xml',
        'views/template.xml',
    ],
    
    "auto_install": False,
    "application": True,
    "installable": True,
    "live_test_url":'https://youtu.be/TTl_2-jipHU',
    "images":["static/description/Banner.png"],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

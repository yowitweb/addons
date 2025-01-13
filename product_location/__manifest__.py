# -*- coding: utf-8 -*-
{
    'name': "Product Location",

    'summary': """
        Display product location on ecommerce product page using google maps.""",

    'description': """
        Product Location module add a new optional field for every product 
        to be displayed on website product page using google maps.
    """,

    'author': "Kusuma Ruslan",
    'website': "http://www.wangsamas.com",
    'support': 'wangsamax@gmail.com',

    'category': 'eCommerce',
    'version': '0.1',
    'application': True,
    "license": "AGPL-3",
    'images': ['static/description/product_location_cover.png'],
#    'price': 10.00,
#    'currency': 'USD',

    'depends': ['sale_management', 'website_sale'],

    'data': [
        'security/ir.model.access.csv',
        'views/quotation_product_location.xml',
        'views/website_sale_location.xml',
        'views/views.xml',
        'demo/demo.xml',
    ],
}
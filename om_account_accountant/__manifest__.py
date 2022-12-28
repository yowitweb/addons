# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Odoo 13 Accounting',
    'version': '13.0.5.0.0',
    'category': 'Accounting',
    'summary': 'Accounting Reports, Asset Management and Account Budget For Odoo13 Community Edition',
    'live_test_url': 'https://www.youtube.com/watch?v=Kj4hR7_uNs4',
    'sequence': '8',
    'website': 'http://odoomates.tech',
    'author': 'Odoo Mates, Odoo SA',
    'maintainer': 'Odoo Mates',
    'license': 'LGPL-3',
    'support': 'odoomates@gmail.com',
    'website': '',
    'depends': ['accounting_pdf_reports', 'om_account_asset', 'om_account_budget'],
    'demo': [],
    'data': [
        'security/group.xml',
        'wizard/change_lock_date.xml',
        'views/account_settings.xml',
        'views/menu.xml',
        'views/account_type.xml',
        'views/account_bank_statement.xml',
        'views/fiscal_year.xml',
        'views/account_coa_template.xml',
        'views/account_group.xml',
        'views/account_tag.xml',
        'views/fiscal_position_template.xml',
        'views/res_partner.xml',
        'views/payment_method.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.png'],
    'qweb': [],
}

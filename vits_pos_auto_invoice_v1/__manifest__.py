# -*- coding: utf-8 -*-
###############################################################################
# Author      : Varanval IT Solutions
# Copyright   : (c) 2025 Varanval IT Solutions. All Rights Reserved.
#
# This software and associated files are the copyrighted property of Varanval IT Solutions.
# Unauthorized copying, redistribution, or modification of any part of this code
# is strictly prohibited unless expressly permitted by the author.
#
# This module is a paid product. It is licensed for use only by the customer
# who has purchased it, and only for the number of users specified at purchase.
#
# For licensing inquiries, contact: markvaranval@gmail.com
###############################################################################
{
    'name': 'Pos Auto Invoice - POS Invoice Auto Check - POS Auto Enable Invoice - Restrict POS Invoice Download',
    'version': '17.1.1',
    'category': 'Point of Sale',
    'sequence': 1,
    'summary': "POS auto invoice | POS invoice download | Auto-generate invoice after payment | Invoice automation for POS | Odoo POS auto invoice | Instant POS invoice creation | Auto billing POS | Invoice on payment POS | Fast POS invoice workflow | Seamless POS invoice integration | POS invoicing tool for Odoo",
    'description': """Automatically generate and download invoices for POS orders right after payment validation. 
            Enable or disable the auto-invoice feature from POS settings. This module simplifies the billing process, saves time, 
            and ensures accurate financial documentation for every transaction. Ideal for retail, restaurant, and fast-moving POS environments. 
            Seamless Odoo 18 integration with no manual steps required. Enhance accounting compliance and improve cashier efficiency with automated invoicing.""",
    'depends': ['base', 'point_of_sale'],
    'keywords': [
        'pos',
        'auto invoice',
        'invoice download',
        'invoice automation',
        'odoo pos invoice',
        'POS invoice download',
        'auto billing',
        'pos customization',
        'point of sale',
        'auto invoice POS',
        'auto invoice generate',
        'pos order invoice',
        'invoice after payment',
        'retail billing automation',
        'odoo pos',
        'odoo'
    ],
    'author': 'Varanval IT Solutions',
    'company': 'Varanval IT Solutions',
    'price': '2.00',
    'currency': 'USD',
    'data': ['views/res_config_settings.xml.xml', ],
    'assets': {
        'point_of_sale._assets_pos': ['vits_pos_auto_invoice_v1/static/src/js/inheri_pos_order.js', ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}

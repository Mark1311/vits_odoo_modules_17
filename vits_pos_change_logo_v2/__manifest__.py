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
    'name': 'Advance POS Change Logo',
    'version': '17.2.2',
    'category': 'Point of Sale',
    'sequence': 1,
    'summary': "Advanced POS logo customization | Set different company logo and POS logo | Change POS logo on screen and receipt | Separate branding for POS interface and receipts | Replace default POS logo in Odoo | POS multi-logo support | Odoo POS branding control | Custom logo display in POS screen and receipts",
    'description': """Upgrade your Odoo POS branding with advanced logo customization. 
                This module allows you to set a separate company logo and POS logo, giving you full control over how your brand appears on the POS screen and printed receipts. 
                Easily upload and update each logo from POS settings to instantly replace the default Odoo logo. 
                Perfect for businesses that want distinct branding for their POS interface and customer-facing receipts. 
                Ideal for retail, restaurants, and multi-outlet setups where professional and consistent branding matters. 
                Seamless integration with Odoo 18 POS — simple to configure, no technical skills required, and changes apply instantly in the next POS session.""",
    'depends': ['base', 'point_of_sale', 'stock'],
    'keywords': [
        'pos change logo',
        'odoo pos logo customization',
        'pos company logo',
        'pos logo and screen saver',
        'change pos logo odoo',
        'pos logo on receipt',
        'custom pos logo',
        'separate company logo pos',
        'odoo pos branding',
        'pos screen logo change',
        'odoo pos interface customization',
        'custom receipt logo pos',
        'pos header logo',
        'pos logo settings',
        'point of sale change logo',
        'odoo pos logo',
        'custom pos receipt',
        'pos logo management',
        'pos branding control',
        'pos screen and receipt logo',
    ],
    'author': 'Varanval IT Solutions',
    'company': 'Varanval IT Solutions',
    'price': '4.00',
    'currency': 'USD',
    'data': [
        'views/res_config_settings.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'vits_pos_change_logo_v2/static/src/xml/inherit_receipt_header.xml',
            'vits_pos_change_logo_v2/static/src/xml/inherit_navbar.xml',
            'vits_pos_change_logo_v2/static/src/js/pos_store.js',
            'vits_pos_change_logo_v2/static/src/js/inherit_receipt_header.js',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}

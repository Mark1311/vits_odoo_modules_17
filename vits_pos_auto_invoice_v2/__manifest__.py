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
    'name': 'Restrict POS Invoice Download | Invoice Automation PRO',
    'version': '17.2.1',
    'category': 'Point of Sale',
    'sequence': 1,
    'summary': "Restrict POS invoice download | POS invoice PDF control | Auto-generate invoice after payment | Odoo POS auto invoice tool | POS invoice auto check | Invoice automation for POS orders | Fast POS billing system | Seamless invoice creation in POS | POS auto invoice generate and download | Prevent invoice PDF download in POS | Auto billing and PDF skip for POS | Odoo 18 POS invoice optimization | Smart POS invoice workflow | POS invoice restrict module for Odoo",
    'description': """Automatically generate POS invoices upon order validation while controlling whether invoice PDFs are downloaded. 
                    Enable or disable both features from POS settings as per your business needs. This module improves billing efficiency, prevents unnecessary 
                    PDF downloads, and keeps your POS system clean and fast. Perfect for high-volume retail, supermarkets, and restaurants. 
                    Fully compatible with Odoo 18 — no manual steps, just smooth automation for a better checkout experience.""",
    'depends': ['base', 'point_of_sale', 'account'],
    'keywords': [
        'restrict pos invoice download',
        'pos invoice pdf control',
        'auto-generate pos invoice',
        'odoo pos invoice automation',
        'invoice automation for pos orders',
        'invoice on payment pos',
        'pos invoice auto check',
        'auto billing pos',
        'prevent invoice pdf download',
        'smart pos invoice workflow',
        'odoo 18 pos invoice module',
        'pos invoice restrict tool',
        'seamless invoice generation',
        'instant pos invoicing',
        'odoo pos pdf skip',
        'billing optimization in pos',
        'pos checkout automation',
        'fast pos invoice creation',
        'odoo 18 pos customization',
        'invoice pdf disable in pos',
    ],
    'author': 'Varanval IT Solutions',
    'company': 'Varanval IT Solutions',
    'price': '5.00',
    'currency': 'USD',
    'data': [
        'views/res_config_settings.xml.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'vits_pos_auto_invoice_v2/static/src/js/inheri_pos_order.js',
            'vits_pos_auto_invoice_v2/static/src/js/inherit_pos_store.js',
            'vits_pos_auto_invoice_v2/static/src/js/inherit_payment_screen.js',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}

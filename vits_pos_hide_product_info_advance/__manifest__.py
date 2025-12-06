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
    'name': 'POS Hide Product Info Advance || POS Hide Product Info Pro',
    'version': '17.1.1',
    'category': 'point_of_sale',
    'sequence': 1,
    'summary': "POS product info icon hider | POS Hide Product Info| Hide Product Info | Product Info | Hide product info button in Odoo POS | Clean and distraction-free POS UI | Remove info tooltip from product cards | Improve POS usability and touch accuracy | Minimal POS interface control | Odoo POS UI customization module | Disable product details icon in POS screen",
    'description': """POS product info icon hider | POS Hide Product Info| Hide Product Info | Product Info | Hide product info button in Odoo POS | Clean and distraction-free POS UI | Remove info tooltip from product cards | Improve POS usability and touch accuracy | Minimal POS interface control | Odoo POS UI customization module | Disable product details icon in POS screen""",
    'depends': ['base', 'point_of_sale', 'stock', 'mail'],
    'keywords': [
        'pos hide product info icon',
        'odoo pos hide info button',
        'hide product info in pos',
        'remove pos product details icon',
        'odoo pos ui cleanup',
        'pos product card customization',
        'hide info icon on pos product card',
        'odoo pos interface control',
        'pos product info visibility',
        'clean pos product card',
        'odoo pos screen customization',
        'minimal pos interface',
        'disable product info button pos',
        'pos ui simplification',
        'odoo pos product tile customization',
        'remove info icon from pos',
        'odoo pos hide details',
        'point of sale product info toggle',
        'pos layout customization',
        'odoo pos icon management',
    ],
    'author': 'Varanval IT Solutions',
    'company': 'Varanval IT Solutions',
    'price': '8.00',
    'currency': 'USD',
    'data': [
        'views/res_config_settings.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'vits_pos_hide_product_info_advance/static/src/xml/inherit_product_info_banner.xml',
            'vits_pos_hide_product_info_advance/static/src/xml/inherit_product_info_popup.xml',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}

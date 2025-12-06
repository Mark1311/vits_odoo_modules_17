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
    'name': 'POS Hide Refund Button',
    'version': '17.1.1',
    'category': 'point_of_sale',
    'sequence': 1,
    'summary': "POS Hide Refund Button | Hide Refund Button in Odoo POS | Remove Refund Action from POS Interface | Clean and focused POS UI | Prevent accidental refunds | Improve POS usability and workflow | Simplify POS interface | Minimal POS screen control | Odoo POS customization module | Hide refund option for selected POS shops",
    'description': """POS Hide Refund Button | Hide Refund Button in Odoo POS | Remove Refund Action from POS Interface | Clean and focused POS UI | Prevent accidental refunds | Improve POS usability and workflow | Simplify POS interface | Minimal POS screen control | Odoo POS customization module | Hide refund option for selected POS shops""",
    'depends': ['base', 'point_of_sale', 'sale', 'stock'],
    'keywords': [
        'pos hide refund button',
        'odoo pos hide refund action',
        'hide refund in pos',
        'remove pos refund button',
        'odoo pos ui cleanup',
        'pos interface customization',
        'hide refund icon pos',
        'odoo pos interface control',
        'pos refund button visibility',
        'clean pos interface',
        'odoo pos screen customization',
        'minimal pos interface',
        'disable refund button pos',
        'pos ui simplification',
        'odoo pos action button control',
        'remove refund action from pos',
        'odoo pos hide action buttons',
        'point of sale refund toggle',
        'pos layout customization',
        'odoo pos button management',
    ],
    'author': 'Varanval IT Solutions',
    'company': 'Varanval IT Solutions',
    'price': '3.50',
    'currency': 'USD',
    'data': [
        'views/res_config_settings.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'vits_pos_hide_refund_button/static/src/xml/inherit_action_pad.xml',
            'vits_pos_hide_refund_button/static/src/xml/inherit_control_button.xml',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}
